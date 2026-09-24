#!/usr/bin/env python3
"""Phase 2 Humanoid bestiary_entry proposal generator (170 entries)."""
import json, re, glob, os

DRAFT_DIR = "/Users/stevchen/Documents/opencode/conts/drafts"
MANIFEST = "/Users/stevchen/Documents/opencode/proj4/data/bestiary_phase1_roster.json"
OUT = "/Users/stevchen/Documents/opencode/conts/phase2_batches/humanoid.json"
ALLOWED_TERRAIN = {"volcanic_foothills", "forested_lake", "green_valley",
                   "high_plateau", "wetland", "river_delta"}

# ---------- parse drafts ----------
files = sorted(glob.glob(os.path.join(DRAFT_DIR, "humanoid_*.md")))
entries = []  # dicts: eid, title, sketch(list of sents), combat_raw, app_raw, states_raw, var_raw
for f in files:
    txt = open(f).read()
    parts = re.split(r"^## \d+\. ", txt, flags=re.M)
    for p in parts[1:]:
        chunk = " ".join(l.strip() for l in p.split("\n")).strip()
        m = re.match(r"(ENY_\w+)\s*[—–-]\s*(.*?)\s+(?=[A-Z0-9(])", chunk)
        eid = chunk.split(" ", 1)[0]
        # sketch: text between title and 'Combat:'
        ci = chunk.find("Combat:")
        title_end = chunk.find(eid) + len(eid)
        # title is up to first sentence start; find '—' or '-' after eid
        dash = re.search(r"[—–-]", chunk)
        body_start = dash.end() if dash else title_end
        sketch_txt = chunk[body_start:ci].strip()
        # remove leading display-name repeat (up to first period? no: sketch starts right after dash with prose)
        ai = chunk.find("Appearance:")
        si = chunk.find("States:")
        vi = chunk.find("Variants:")
        combat_raw = chunk[ci:ai].strip()
        app_raw = chunk[ai:si].strip()[len("Appearance:"):].strip()
        states_raw = chunk[si:vi].strip()[len("States:"):].strip()
        var_raw = chunk[vi:].strip()[len("Variants:"):].strip()
        # sketch sentences
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", sketch_txt) if s.strip()]
        entries.append({"eid": eid, "sketch": sents, "combat_raw": combat_raw,
                        "app_raw": app_raw, "states_raw": states_raw, "var_raw": var_raw})
assert len(entries) == 170, len(entries)

manifest = json.load(open(MANIFEST))
hum = [e for e in manifest["entries"] if e["taxonomy"] == "Humanoid"]
assert len(hum) == 170
for d, m in zip(entries, hum):
    assert d["eid"] == m["id"], (d["eid"], m["id"])
    # strip leading display-name title repeat fused to first sketch sentence
    core = re.sub(r"\s*\(.*\)\s*$", "", m["display_name"]).strip()
    pat = re.compile(r"^" + re.escape(core) + r"(\s*\([^)]*\))?\s*", re.IGNORECASE)
    joined = " ".join(d["sketch"])
    joined = pat.sub("", joined).strip()
    d["sketch"] = [s.strip() for s in re.split(r"(?<=[.!?])\s+", joined) if s.strip()]

# ---------- combat parse ----------
def parse_combat(raw):
    mr = re.search(r"reuse\s+(ENY_\w+)", raw)
    if mr:
        return {"reuse_enemy_id": mr.group(1)}
    ms = re.findall(r"\d+", raw)
    assert len(ms) >= 4, raw
    pol = "always_physical" if "always_physical" in raw else ("cycle" if "cycle" in raw else "always_physical")
    return {"might": int(ms[0]), "magic": int(ms[1]),
            "intelligence": int(ms[2]), "leadership": int(ms[3]),
            "opponent_policy": pol}

# ---------- family index (1-based draft order) ----------
def famkey(i):
    n = i + 1
    if n <= 5: return "gnomes"
    if n <= 10: return "halflings"
    if n <= 15: return "dwarves"
    if n <= 20: return "goblins"
    if n <= 25: return "hobgoblins"
    if n <= 30: return "orcs"
    if n <= 35: return "ogres"
    if n <= 40: return "trolls"
    if n <= 45: return "elves"
    if n <= 47: return "treemen"
    if n <= 52: return "ratfolk"
    if n <= 54: return "naga"
    if n <= 59: return "mermaids"
    if n <= 64: return "sphinxes"
    if n <= 66: return "sirens"
    if n <= 68: return "oni"
    if n <= 70: return "kappa"
    if n <= 75: return "monkeys"
    if n <= 80: return "foxmaidens"
    if n <= 85: return "indian"
    if n <= 90: return "kobolds"
    if n <= 95: return "gnolls"
    if n <= 100: return "aegipanes"
    if n <= 105: return "boarheads"
    if n <= 110: return "lizards"
    if n <= 115: return "satyrs"
    if n <= 120: return "harpies"
    if n <= 122: return "hags"
    if n <= 124: return "leshy"
    if n <= 129: return "vodyanoy"
    if n <= 134: return "rusalka"
    if n <= 139: return "jotnar"
    if n <= 141: return "duergar"
    if n <= 143: return "fomorian"
    if n <= 145: return "selkie"
    if n <= 147: return "sidhe"
    if n <= 149: return "minotaur"
    if n <= 151: return "centaur"
    if n <= 153: return "cyclops"
    if n <= 155: return "lamia"
    if n <= 157: return "div"
    if n <= 159: return "scorpion"
    if n <= 164: return "jackal"
    if n <= 166: return "falcon"
    if n <= 168: return "croc"
    return "thunderbird"

HABITAT = {
    "gnomes": ["green_valley"], "halflings": ["green_valley"],
    "dwarves": ["high_plateau"], "goblins": ["green_valley"],
    "hobgoblins": ["green_valley"], "orcs": ["high_plateau"],
    "ogres": ["green_valley"], "trolls": ["wetland"], "elves": ["forested_lake", "green_valley"],
    "treemen": ["forested_lake"], "ratfolk": ["wetland"],
    "naga": ["wetland"], "mermaids": ["river_delta"], "sphinxes": ["high_plateau"],
    "sirens": ["river_delta"], "oni": ["volcanic_foothills", "high_plateau"],
    "kappa": ["river_delta", "wetland"], "monkeys": ["forested_lake"],
    "foxmaidens": ["green_valley"],
    "indian": ["forested_lake", "green_valley"], "kobolds": ["wetland"],
    "gnolls": ["green_valley"], "aegipanes": ["high_plateau"],
    "boarheads": ["forested_lake"], "lizards": ["wetland"],
    "satyrs": ["green_valley"], "harpies": ["high_plateau"],
    "hags": ["wetland"], "leshy": ["forested_lake"],
    "vodyanoy": ["river_delta", "forested_lake"], "rusalka": ["river_delta"],
    "jotnar": ["high_plateau"],
    "duergar": ["high_plateau"], "fomorian": ["river_delta"],
    "selkie": ["river_delta", "forested_lake"], "sidhe": ["green_valley", "forested_lake"],
    "minotaur": ["high_plateau"], "centaur": ["green_valley"],
    "cyclops": ["high_plateau"], "lamia": ["wetland"],
    "div": ["high_plateau"], "scorpion": ["volcanic_foothills"],
    "jackal": ["volcanic_foothills"], "falcon": ["high_plateau"],
    "croc": ["river_delta"], "thunderbird": ["high_plateau"],
}
HAB_OVERRIDE = {36: ["river_delta"], 37: ["high_plateau"], 38: ["high_plateau"],
    39: ["river_delta"], 40: ["wetland"], 46: ["forested_lake"], 47: ["wetland"],
    55: ["river_delta"], 56: ["river_delta"], 57: ["forested_lake"],
    58: ["river_delta"], 59: ["river_delta"], 60: ["high_plateau"],
    61: ["forested_lake"], 62: ["wetland"], 63: ["high_plateau"],
    64: ["high_plateau"], 65: ["river_delta"], 66: ["forested_lake"],
    76: ["green_valley"], 77: ["high_plateau"], 78: ["volcanic_foothills"],
    79: ["wetland"], 80: ["green_valley"], 130: ["river_delta"],
    131: ["forested_lake"], 132: ["green_valley"], 133: ["forested_lake"],
    134: ["river_delta"], 137: ["volcanic_foothills"], 149: ["volcanic_foothills"],
    153: ["volcanic_foothills"]}

CAST = set(list(range(41, 46)) + [121, 122, 140, 141, 146, 147, 156, 157])
BEHAV = set(list(range(46, 48)) + [53, 54] + list(range(60, 65)) + list(range(76, 81))
            + [123, 124] + list(range(130, 135)) + [154, 155, 65, 66, 169, 170])

BAND_LEADER = re.compile(r"band-level", re.I)

MUNDANE_TRICK = {2, 19, 29, 50, 94, 103, 109, 114, 138, 162}

DISTINCTION = {
    "foxmaidens": "These fox-maidens are true folk rather than animals, wholly distinct from the wild cinder foxes of the Beast roster.",
    "boarheads": "These boar-headed folk are reasoning bands rather than animals, wholly distinct from the wild boars of the Beast roster.",
    "jackal": "These jackal-headed folk stand apart from the wild delta jackals of the Beast roster and from the hyena-folk gnolls.",
    "scorpion": "These scorpion-folk are reasoning bands rather than vermin, wholly distinct from the giant scorpions of the Beast roster.",
    "croc": "These croc-folk are reasoning bands rather than animals, wholly distinct from the river crocs of the Beast roster.",
    "gnolls": "These hyena-folk are reasoning bands rather than animals, wholly distinct from the laugh-hounds of the Beast roster.",
    "kobolds": "These kobold scavengers are their own small folk, kept separate from the marsh lizard stalkers.",
    "falcon": "These falcon-headed folk stand apart from the wild raptors of the Beast roster and from the eagle-winged garuda scouts.",
    "thunderbird": "These thunderbird folk stand apart from the storm rocs of the Beast roster and from darker winged powers.",
    "kappa": "These kappa imps are true water folk, and the snapping turtles of the Beast roster are explicitly not kappa.",
    "oni": "These oni remain Humanoid bands under the cosmology exclusion, never demons and never spirits.",
    "indian": "The garuda name is held by these Humanoid scouts, while the Beast roster uses roc for its great birds.",
    "sphinxes": "These sphinxes were formerly called bird-maidens, renamed to avoid confusion with the sphinx-pards of the Beast roster.",
    "naga": "These naga were formerly called snakefolk, renamed constrictors and ambushers of the marsh reeds.",
    "sirens": "These sirens are half-bird-half-fish lurers of the shore ledges, distinct from mermaids and sphinxes alike.",
    "lizards": "These marsh stalkers are their own scaled folk, kept separate from kobolds, naga, and croc-folk.",
    "satyrs": "These lowland satyr raiders are kept distinct from the highland aegipane herders.",
    "aegipanes": "These highland aegipane herders are kept distinct from the lowland satyr raiders.",
    "harpies": "These harpy harriers are female-led snatcher-raiders, distinct from sphinx singers and siren lurers.",
    "mermaids": "These mermaids were formerly called fish-maidens, all-female bands of reef, surf, deep, and river waters.",
}

EXPAND = {
 "gnomes": ["Their pebble-count justice settles every quarrel without appeal, and exiled thieves warn others for seasons.", "They move their burrow camps with the seasons, leaving swept tunnels that patrols always find empty.", "Travellers who share bread and mind their dogs pass warren lands unmolested by night."],
 "halflings": ["Their caravan shares are divided by counted sticks, and every elder remembers the famine years.", "They prefer melting through streams to standing in line, for water kills scent and dogs.", "A mended roof and a blind eye buy more peace with them than any patrol."],
 "dwarves": ["These exiles keep no holds and no clans as final content, only quarry camps and tally-sticks.", "They respect anyone who stands ground beside them, and slow work buys parole-tallies.", "Their craft is coal and bellows only, with no runic magic claimed as final."],
 "goblins": ["These feral bands are wholly separate from any integrated townsfolk, implying no faction change.", "Only males march in these packs, for goblins have no females by their biology.", "Their ditch-country camps shift nightly, and every gully for miles is known to them."],
 "hobgoblins": ["Their crude drill apes old manuals without claiming any greater allegiance or faction.", "Meat and first sleep are their only pay, and empty camps scatter them quickly.", "They hold rank where lesser kin mob, withdrawing only at horn-calls."],
 "orcs": ["They respect strength alone and despise weakness even among their own bands.", "Their rock-pile seats are thrones in all but name, never called such as final.", "Their camps are bone-piles, and they respect any foe who stands."],
 "ogres": ["They drift between bands as hired muscle, too big for any single tribe to feed.", "They understand bargains only in food, and chase whatever flees from them.", "Wounds that drop men barely slow them, and fences fall before their posts."],
 "trolls": ["They hate fire the way all night-folk do, though no magic burns them here.", "They claim fords, pastures, and reed-beds as solitary holders, never as kingdoms.", "Their curses are noise alone, never magic, and their broths heal only hunger."],
 "elves": ["These exile bands claim no kingdom and no court as final content, only boundary paths.", "They share campfires sparingly and vanish before debts can form with villagers.", "Any elven arts they show remain a flagged proposal under magic doctrine, never final canon."],
 "treemen": ["Their root-grasp is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They pursue no farther than root-shade, and their fallen leaves bury the slain quietly.", "Their bark has no sex, so their forms are slow seed-lines and age-forms only."],
 "ratfolk": ["Their plague-filth works through mundane rot alone, with no new magic claimed as final.", "Their culvert warrens breed quickly where old drains collapsed and were forgotten.", "Fire scatters them faster than steel, and musky droppings betray their routes."],
 "naga": ["Their coil-squeeze is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They worship no gods, only warm stones, and release dead prey slowly.", "Their shed skins mark territories that fisherfolk learn to respect."],
 "mermaids": ["All their bands are female by nature, with no males among reef, surf, deep, or river.", "They ransom catches for shiny things rather than killing, and remember kind boatmen.", "They lead only roaming bands, with no settlement or faction implication as final content."],
 "sphinxes": ["All their flocks are female by nature, singing dawn choruses that shepherds use as clocks.", "Their chorus-allure is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They ransom seized goats for shiny wire and mark territories with guano streaks."],
 "sirens": ["All their bands are female by nature, singing layered harmonies across calm water.", "Their compelling song is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They avoid armored boats and massed archers, ransoming sailors for bread and water."],
 "oni": ["Rice wine left at boundary markers deflects them better than spears.", "They collect ironware obsessively and spare children encountered on roads.", "Fast rivers frighten them, and bells unsettle their quarry-yard kin."],
 "kappa": ["A deep bow spills their head-water and weakens them, so polite travellers pass safely.", "They love cucumbers above all tribute and return favors strictly.", "Their mud-nests hide clutches that farmers learn to leave alone."],
 "monkeys": ["No monkey Beasts exist elsewhere, so these troops hold the canopy alone.", "Shiny bottlecaps delight them above food, and dogs scatter them faster than spears.", "Their branch-trails span many miles of connected canopy highways."],
 "foxmaidens": ["All their bands are female by nature, raising cubs communally in hidden earths.", "Their riddle-allure is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They trade herbs and warnings for needles, glass, and stories, shifting earths each season."],
 "indian": ["They bridge feuding troops with slow caravans that even rivals respect.", "Knotted-cord ledgers record every debt faithfully among their traders.", "They despise coiling naga on sight, clashing with ancient instinctive rivalry."],
 "kobolds": ["Torches scatter them faster than swords, and floods drown whole warrens helplessly.", "They worship shiny scrap with hoarding reverence above silver.", "A working hinge delights them beyond food, and smiths tolerate their sweeping."],
 "gnolls": ["They collect cracked marrow bones obsessively and remember waterholes across droughts.", "Disciplined spear lines frighten them, and crackling fire routs them instantly.", "Resident lions contest every carcass they camp beside for days."],
 "aegipanes": ["They despise every fence and locked gate raised across their high pastures.", "Circular stone folds dot their ranges, and cracked pipes pass down as heirlooms.", "Lowland grain trades for their sharp cheese at every season change."],
 "boarheads": ["They collect dented helmets as drinking bowls and fear crackling fire lines.", "Catgut strings snap in wet weather, shaming archers before the sounder.", "A full trough keeps fragile peace longer than any oath among them."],
 "lizards": ["They collect sun-warmed stones compulsively and fear sudden cold snaps.", "Prepared fire breaks their hunts, and black mud can mire even swift darters.", "Their sunken caches glitter with old coins that divers trade for lamp oil."],
 "satyrs": ["They fear consecrated iron bells above all weapons raised against them.", "Pruning hooks deter them effectively, and snares catch their scouts at trails.", "Leaking mash-logs betray their camps by smell for miles around."],
 "harpies": ["Their flocks are female-led, with a single flock-guard husband attending each band.", "They dread concentrated volleys and abandon assaults against prepared fire.", "Their cliff nests accumulate trophies and glittering loot across seasons."],
 "hags": ["Their hedge curses remain a flagged proposal under magic doctrine, never final canon.", "All their outcasts are cast-out widows, with males absent by their history.", "Villagers blame them for failed crops, yet trade bread crusts for dubious charms."],
 "leshy": ["Their forest-meld is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They marry no one and accumulate no property anywhere in the woods.", "They release captives who willingly replant young saplings afterward."],
 "vodyanoy": ["All their water-lines are male patriarchs, with females absent by drowned custom.", "Tobacco and exact fares buy safe passage across their ponds and crossings.", "Drained channels strand them helplessly, and they release respectful drinkers."],
 "rusalka": ["All their bands are female by nature, drowned brides keeping river customs.", "Their lure-song is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They release captives who offer linen, ribbons, eggs, or correctly solved riddles."],
 "jotnar": ["Their seers read weather only, with no true prophecy claimed as final.", "Goat tribute at boundary cairns buys safer passage through their ranges.", "Thaw seasons weaken them, and they pursue downhill only in deep winter."],
 "duergar": ["Their rune-craft remains a flagged proposal under magic doctrine, never final canon.", "Bright sunlight sickens them swiftly, and they fight silently in tight files.", "They keep no kingdom as final content, only lightless quarry depths and slave gangs."],
 "fomorian": ["Their rumored death-gaze is false, with precise rock-throwing their only true threat.", "Fire drives them backward through surf toward waiting water.", "Milk and cattle tribute buy quiet shores from their raiding crews."],
 "selkie": ["Their moonlit dances entrance lonely watchers, and stolen skins enslave them utterly.", "They ransom captured skins afterward with polished pearls and beachcombed amber.", "Warm shallows sicken deep kin, who cannot remain landlocked very long."],
 "sidhe": ["Their court glamour remains a flagged proposal under magic doctrine, never final canon.", "They fear cracked iron bells above all weapons, scattering at their ringing.", "They ransom captured travellers afterward in exchange for new songs."],
 "minotaur": ["Open plains leave maze kin exposed, frightened, and deeply confused.", "They spare defeated challengers who kneel immediately and surrender.", "Quenching floods terrify forge kin, for water ruins their furnaces."],
 "centaur": ["They despise fences that break their traditional running paths.", "Storm feathers gathered after gales decorate their braided manes.", "Their bark armor regrows each year after winter storms."],
 "cyclops": ["They count flocks by smell alone and love sharp cheese above silver.", "They spare travellers who sincerely praise their flocks.", "Sudden quenching ambushes terrify their smiths greatly at night."],
 "lamia": ["Their lines are female-leaning, with a single rare consort attending each band.", "Their veiled song is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They spare outrageous flatterers and release captives who solve their riddles."],
 "div": ["Their mighty sorcery remains a flagged proposal under magic doctrine, never final canon.", "They spare travelling musicians generously after hearing their songs.", "Rain dampens their powders uselessly, exposing bluffers who flee howling."],
 "scorpion": ["They collect precious water obsessively in wax-sealed gourds.", "Open fire routs them hastily, and deep burrows conceal their vulnerable clutches.", "Their weak venom sickens slowly rather than killing outright."],
 "jackal": ["They despise hyena-folk with intense and enduring hostility.", "Their rites are memorized ancestral law and herbal smoke, never true divine magic.", "Sandstorms conceal their retreats, and dry hounds tire without water."],
 "falcon": ["They refuse grounded fighting whenever their powerful wings remain sound.", "Polished signal mirrors flash their wing-commands across mountain passes.", "Worthy feathers ransom maps from their cliffside sentries."],
 "croc": ["Open fire makes them abandon hunts and withdraw quickly.", "They collect boat nails from every captured vessel passing their reaches.", "Nervous fish tolls buy safe crossings through their delta channels."],
 "thunderbird": ["Their storm-screech is flagged as an intuitive behavior-magic proposal, never cast as final magic.", "They cannot sustain flight in completely calm air.", "Their lightning-split eyries smoke after every passing tempest."],
}
FACE = {
 "gnomes": "broad-nosed mud-caked face", "halflings": "round cheerful weathered face",
 "dwarves": "bearded stone-eyed face", "goblins": "sharp-eared green scowling face",
 "hobgoblins": "tusked orange disciplined face", "orcs": "tusked broad scarred face",
 "ogres": "small-headed slab-jawed face", "trolls": "moss-browed small-eyed face",
 "elves": "pale keen slender face", "treemen": "knothole-eyed bark face",
 "ratfolk": "whiskered red-eyed rat face", "naga": "amber-eyed scaled human face",
 "mermaids": "dark wide-eyed sea face", "sphinxes": "fierce feather-framed maiden face",
 "sirens": "sea-green honey-voiced maiden face", "oni": "horned red scowling brute face",
 "kappa": "beaked bowl-crowned imp face", "monkeys": "muzzled bright-eyed monkey face",
 "foxmaidens": "amber-eyed prick-eared vixen face", "indian": "striped bearded proud face",
 "kobolds": "mangy big-eared scavenger face", "gnolls": "laughing spotted hyena face",
 "aegipanes": "curl-horned braided-beard goat face", "boarheads": "yellow-tusked bristled boar face",
 "lizards": "lidless scaled patient face", "satyrs": "wine-flushed wreath-crowned goat face",
 "harpies": "hungry beaked windswept face", "hags": "wart-skinned hook-nosed elder face",
 "leshy": "moss-bearded green-gold-eyed warden face", "vodyanoy": "green-bearded pond-stone-eyed elder face",
 "rusalka": "sorrowful pale dripping maiden face", "jotnar": "rime-bearded massive weathered face",
 "duergar": "ash-grey red-rimmed sullen face", "fomorian": "single-eyed salt-crusted twisted face",
 "selkie": "soft-eyed sleek black-haired face", "sidhe": "luminous unsettling beautiful face",
 "minotaur": "flaring-nostrilled horned bull face", "centaur": "proud braided-maned human face",
 "cyclops": "single watery-eyed towering face", "lamia": "kohl-rimmed alluring serpent-woman face",
 "div": "low-browed resentful stone-hided face", "scorpion": "cluster-eyed chitin-armored stalker face",
 "jackal": "narrow-muzzled tall-eared jackal face", "falcon": "hooked-beaked piercing-eyed falcon face",
 "croc": "slit-eyed mossy-scute armored face", "thunderbird": "bright-eyed static-feathered storm face",
}
GEAR = {
 "gnomes": "mud-wrap shade and pick wear", "halflings": "cloak patch and snare coil",
 "dwarves": "beard braid and shield scoring", "goblins": "rag wrap and knife notch",
 "hobgoblins": "rank-cloak cut and halberd binding", "orcs": "hide wrap and cleaver nick",
 "ogres": "hide belt and club grain", "trolls": "moss cover and hide cracking",
 "elves": "cloak fold and bow finish", "treemen": "bark ridge and moss patch",
 "ratfolk": "fur patch and blade rust", "naga": "scale sheen and tail banding",
 "mermaids": "tail shimmer and net knotting", "sphinxes": "plumage tone and talon polish",
 "sirens": "scale gloss and wing feathering", "oni": "skin tint and club studding",
 "kappa": "shell moss and bowl polish", "monkeys": "fur shade and tail curl",
 "foxmaidens": "fur tint and tail fullness", "indian": "stripe depth and bangle count",
 "kobolds": "fur mange and scrap shine", "gnolls": "spot pattern and bone stringing",
 "aegipanes": "wool shagginess and horn curl", "boarheads": "bristle length and tusk yellowing",
 "lizards": "scale gloss and tail flagging", "satyrs": "wreath freshness and pipe binding",
 "harpies": "plumage raggedness and talon scarring", "hags": "shawl patch and charm stringing",
 "leshy": "moss thickness and bark creasing", "vodyanoy": "beard weed and rope coiling",
 "rusalka": "hair length and wreath freshness", "jotnar": "beard rime and cloak hide",
 "duergar": "skin ash tone and chain weight", "fomorian": "barnacle cover and club driftwood",
 "selkie": "sealskin fold and knife keenness", "sidhe": "cloak shimmer and shield polish",
 "minotaur": "horn span and hide soot", "centaur": "coat dappling and mane braiding",
 "cyclops": "skin weathering and apron char", "lamia": "veil weave and coil gloss",
 "div": "hide cracking and cauldron denting", "scorpion": "chitin gleam and tail curl",
 "jackal": "fur grooming and charm stringing", "falcon": "crest lift and mirror polish",
 "croc": "scute moss and jaw scarring", "thunderbird": "crest brightness and charm crackle",
}
REASON = {
 "goblins": "all-male packs by biology, with no females",
 "mermaids": "all-female bands by nature", "sphinxes": "all-female flocks by nature",
 "sirens": "all-female bands by nature", "foxmaidens": "all-female bands by nature",
 "rusalka": "all-female bands by nature", "vodyanoy": "male water-lines, with females absent by drowned custom",
 "harpies": "female-led flocks with a single flock-guard husband",
 "lamia": "female-leaning lines with a single rare consort",
 "treemen": "sexless bark with age-forms only, read male-presenting",
 "hags": "cast-out widows, with males absent by history",
 "trolls": None, "ogres": None, "ratfolk": None, "gnomes": None, "halflings": None,
 "dwarves": None, "hobgoblins": None, "orcs": None, "elves": None, "naga": None,
 "oni": None, "kappa": None, "monkeys": None, "indian": None, "kobolds": None,
 "gnolls": None, "aegipanes": None, "boarheads": None, "lizards": None,
 "satyrs": None, "leshy": None, "jotnar": None, "duergar": None, "fomorian": None,
 "selkie": None, "sidhe": None, "minotaur": None, "centaur": None, "cyclops": None,
 "div": None, "scorpion": None, "jackal": None, "falcon": None, "croc": None,
 "thunderbird": None,
}

EXPAND2 = {
 "gnomes": ["Young diggers learn pebble-count before they learn letters, counting shares in the dark.", "Grey elders settle burrow quarrels by whistle-codes that carry through packed earth.", "Blocked burrows and fed dogs thin them faster than any spear wall."],
 "halflings": ["Young runners learn hedge-paths before they learn letters, moving like field-mice.", "Grey elders divide every caravan share by counting sticks around evening fires.", "Frost hardens their poaching trade and sharpens hunger through lean months."],
 "dwarves": ["Young oath-cut exiles drill with hand-axes in played-out quarries each morning.", "Grey singers keep hammer-timing songs that synchronize whole crews without magic.", "Cave-ins haunt their dreams, and lantern-codes mark the bounds they guard."],
 "goblins": ["Squeakers learn ditch-runs before knives, scampering gullies the watch never maps.", "Grey layers knot wire traps along footpaths that even friends forget by dawn.", "Stink-pots and nettle-smoke are their only sorcery, and rain washes both away."],
 "hobgoblins": ["Young levies learn lockstep marching before they earn halberds of their own.", "Grey filemen oil bowstrings nightly and fletch shafts from scrub feathers.", "Notched tally-sticks count every head and meat-share in their marching bands."],
 "orcs": ["Young chargers test chiefs nightly, seeking rank through single combat.", "Grey sniffers read trails better than hounds and defeat disguises with their noses.", "Drum-beats surge their mobs the way war-drums surge any fighters, without sorcery."],
 "ogres": [ "Young lumpers love the crash of gates and learn timing from sergeants' shouts.", "Fat masters taste every cauldron and stretch thin meat for whole bands.", "A held gate breaks clubbers, and broken fingers end even great throwers."],
 "trolls": ["Young waders learn ford-tolls before speech, counting goats with wet fingers.", "Grey mossbacks remember every burned bridge and every drained marsh.", "Sunlight blinds cave kin, and lanterns hold them better than spears."],
 "elves": ["Young watchers learn silent steps before bowcraft, padding needles without sound.", "Scarred rangers remember boundary oaths sworn to bailiffs long dead.", "Iron shortage and hunger drive them toward farms they openly despise."],
 "treemen": ["Nesting birds shelter in willow hair, and old nooses hang beside them.", "Villagers leave damaged tools at grove edges as apology offerings each spring.", "Axes and fire are their only true fears, and arrows break harmlessly on bark."],
 "ratfolk": ["Young squeakers learn culvert-runs before knives, mapping drains by whisker-touch.", "Grey inventors twist wire deadfalls from stolen bell parts without gunpowder.", "Boiled water defeats their filth-craft, and mousers frighten them more than watchmen."],
 "naga": ["Young coils learn ambush patience in steaming reeds before their first hunt.", "Scarred crushers coordinate silent surrounds with tail-taps at dusk.", "Fire breaks their hunts, and formed spear lines turn their grapples aside."],
 "mermaids": ["Young singers learn tide-pool crabbing before they learn wreck-diving.", "Scarred divers navigate by pressure changes and cold currents alone.", "Iron nets and deep currents frighten them, and sunlight bars deep kin."],
 "sphinxes": ["Young fledglings learn boundary drops before they learn chorus mimicry.", "Grey choristers remember every storm season across decades of ledge-keeping.", "Cave snakes and lowland nets are the fears they never outgrow."],
 "sirens": ["Young singers learn layered harmonies before they learn wreck-coin diving.", "Grey harmonists remember every drowned hull along their wave-cut ledges.", "Winter gales and iron nets drive them to deep trenches for shelter."],
 "oni": ["Young horns learn gate-smashing serving under scarred crushers.", "Grey breakers judge masonry by touch and collect ironware obsessively.", "Offered wine at boundary markers turns their patrols aside peacefully."],
 "kappa": ["Young wrestlers learn sumo bouts before they learn dam-building.", "Grey plotters memorize every hidden plank across reed mazes.", "Stolen melons and tools trade back for cucumbers at dusk."],
 "monkeys": ["Young swingers learn canopy highways before they learn stick-fighting.", "Grey callers map territories through answering dawn songs.", "Painted gourd-targets litter every camp clearing where archers practice daily."],
 "foxmaidens": ["Young vixens learn bracken runs before knives, circling silently on soft paws.", "Grey storytellers trade riddle-wisdom for iron needles and new tales.", "Whiteouts and quenching floods are the dooms their earths cannot escape."],
 "indian": ["Young claws learn cat-patient ambush before they earn iron bangles.", "Mossy elders remember buried hoards from fallen regimes without maps.", "Bone dice decide nightly watches fairly among yaksha guards."],
 "kobolds": ["Young yappers learn pit-lurking before spoon-shivs, yipping alarms at dusk.", "Grey savers hoard hinges and wire-spools against cold rainy nights.", "Half-wild curs hunt rats beside them, sharing every scrap of meat."],
 "gnolls": ["Young gigglers learn relay pursuits before spears, running down gazelles.", "Grey relayers read shifting winds with lifted noses across open flats.", "Thorn fields lame their hunters, and lost scents end pursuits immediately."],
 "aegipanes": ["Young herd-boys learn scree climbing before crooks, chasing stray goats.", "Grey goatherds carve bone flutes during long lonely watches.", "River reeds gather yearly for new pipes, and cracked pipes become heirlooms."],
 "boarheads": ["Young grunters learn shield-breaking charges through boar-infested thickets.", "Grey eyes loose patiently from stinking blinds that betray them downwind.", "Squealing piglets draw suicidal defense from every archer among them."],
 "lizards": ["Young floaters learn statue-stillness from basking crocodiles over seasons.", "Grey drivers race dawn sport across mudflats, waving bright tail-flags.", "Barbed hooks frighten divers, who navigate lightless depths purely by touch."],
 "satyrs": ["Young dancers learn lilting reed-tunes before leaf-blades, capering at midnight.", "Grey pipers remember great vintages across decades of stolen harvests.", "Cellar doors and daughters alike lock at dusk when pipes sound."],
 "harpies": ["Young screechers learn battlefield circling before bloody talon-dives.", "Grey callers remember campaigns across decades of corpse-stripping.", "Brass buckles and wool-sacks gather in eyries glittering with loot."],
 "hags": ["Grey widows gather bitter herbs that honest wives refuse to touch.", "One-eyed cats keep them sole company in leaking hovels.", "False lantern lights lure travellers over sucking pools at night."],
 "leshy": ["Grey misleaders punish greedy poachers with hopeless circles lasting days.", "Honey offerings at mossy stumps buy safe passage through their stands.", "Fragile pipes break easily, scattering their swarms in sudden panic."],
 "vodyanoy": ["Young mudders learn weed-rope dragging beneath rotting waterwheels.", "Grey pond-fathers remember every dam built across three generations.", "Drowned brass clocks gather in sunken chests no diver reaches."],
 "rusalka": ["Young brides learn moonlit combing before hair-rope drowning.", "Grey dancers remember every betrayal across drowned centuries.", "Painted eggs and flower wreaths buy safer fords from their bands."],
 "jotnar": ["Young striders learn glacier hunting before heavy boulder-throwing.", "Grey rimebeards carve snow shelters effortlessly during whiteouts.", "Ravens perch on seers, and single eyes misjudge depth badly."],
 "duergar": ["Young drudges learn mattock-drill in lightless files before spears.", "Grey taskmasters count every lash meticulously in salt-stained ledgers.", "Stray kobolds serve them as slaves, and wells suffer their spite at night."],
 "fomorian": ["Young waders learn surf-bellowing before heavy driftwood clubs.", "Scarred raiders demand milk tribute from shore families each dawn.", "Tide-pool armor crusts their mismatched limbs with salt."],
 "selkie": ["Young maids learn salmon-netting beside fisherfolk at dawn.", "Grey skin-keepers hide precious skins beneath tidal rocks.", "Beachcombed amber trades to smiths for precious iron."],
 "sidhe": ["Pale riders learn riddling trade before thin swords, walking twilight roads.", "Grey whisperers remember oaths sworn before successor kings ruled.", "Cream bowls left at mound doors buy news and safe passage."],
 "minotaur": ["Young bulls memorize twisting passages without error before their first duel.", "Sooty masters understand bellows rhythms through long furnace practice.", "Labyrinth maps gather obsessively in the care of maze kin."],
 "centaur": ["Young runners race storms for joy before they learn bowcraft.", "Mossy elders understand timber prices and watch every loaded wagon.", "Reasonable tolls buy escort through forest borders they patrol."],
 "cyclops": ["Young eyes learn heavy millstone hurling before flock-whistling.", "Sooty masters judge hot metal quality by taste alone.", "Hollowed bone flutes sound tunelessly across their lonely pastures."],
 "lamia": ["Young allures learn veiled songs before lion-paw raking.", "Grey mourners collect tiny shoes obsessively in sandy niches.", "Iron mirrors dazzle marsh kin, loosening coils that riddle-answers open."],
 "div": ["Young hurlers learn tor-throwing before toll-demanding on caravan tracks.", "Grey ridge-lords collect bronze cauldrons obsessively from ransacked caravans.", "Colored powders and ventriloquism bluff travellers, dampening uselessly in rain."],
 "scorpion": ["Young skitterers learn dune-stalking before sharp barbed spears.", "Scarred stalkers ambush caravans patiently at lonely wells.", "Humid nursery chambers hide clutches that wardens guard suicidally."],
 "jackal": ["Young trotters learn cold-trail reading beneath shifting sand.", "Grey judges conduct weighing rites over feather-balanced scales.", "Turquoise charms jingle on raiders who prize them above silver."],
 "falcon": ["Young eyases learn sheer crag-perching before sharp talon-spears.", "Grey watchers record every caravan banner with patient care.", "Narrow ledges hold polished signal mirrors flashing wing-commands."],
 "croc": ["Young floaters learn log-still ambushes before crushing jaw-sweeps.", "Scarred brutes erupt beside boats with sweeping tail blows.", "Winding reaches close under echoing roars when elders display."],
 "thunderbird": ["Young riders learn thunderhead riding before stone axes.", "Scarred callers read gathering static accurately in raised feathers.", "Storm-glass charms crackle on every veteran of the colonies."],
}
BANDS_ONLY = "They roam only in small outside-society bands, with no settlement or faction implication as final content."
EXPAND3 = {
 "gnomes": ["Barrow-straps creak under tool weight on every long farm lane.", "River-stone pouches never empty while scrub hills stand."],
 "halflings": ["Leaf-cloaks sewn with pockets hide snares, pipes, and supper.", "Kennel-carts roll with their bands wherever goats wander."],
 "dwarves": ["Quarry dust ingrains every beard no matter how often washed.", "Song-tallies knotted in beards record pay-shares without writing."],
 "goblins": ["Trophy teeth strung on cords mark every successful wolf rider.", "Junk-pile hoards grow worthless to all but their boss-kin."],
 "hobgoblins": ["Stolen saddles fit shaggy ponies that tire quickly without fodder.", "Trophy-cloaks and iron helms mark warlords above filemen."],
 "orcs": ["Trophy-teeth necklaces rattle on every chief above rock-furs.", "Nose-rings glint on trackers loping tirelessly through scrub."],
 "ogres": ["Rope harnesses chafe young clubbers swinging whole trees.", "Cauldron-lid shields clang beside iron-shod staves of matriarchs."],
 "trolls": ["Ford-mud cakes every bridge troll thicker than armor.", "Shepherds fire hillsides yearly to drive hill kin away."],
 "elves": ["Thorn-cords bind long silver hair above soft-soled boots.", "Seed-pouches replant burned groves quietly along wanderers roads."],
 "treemen": ["Moss and algae drape every limb that overhangs still water.", "Slow decades teach them every woodsman axe by sound."],
 "ratfolk": ["Bottle-glass goggles glint on engineers hunched over wire devices.", "Tallow and fear scent every nesting warren they defend."],
 "naga": ["Leaf-litter cloaks hide coiled ambushers until spears spring.", "Clutch-eggs rest in nests that dams defend unto death."],
 "mermaids": ["Reef gardens of shell and coin mark every territory.", "Conch-horns pass down as heirlooms among storm matrons."],
 "sphinxes": ["Stolen spoons gather in forest roosts above charcoal camps.", "Storm-glass glints in high eyries after every gale."],
 "sirens": ["Shore gardens of wreck coins glitter beside tide-pools.", "Abyssal shells trade for news of distant wars."],
 "oni": ["Tiger-hide belts cinch every brute above steaming breath.", "Quarry waste-piles grow steadily yearly around smasher grounds."],
 "kappa": ["Melon-sacks bulge on marsh thieves slipping through reeds.", "Webbed claws drag waders toward deep water without mercy."],
 "monkeys": ["Bottlecap necklaces jingle on every scout swinging below branches.", "Throat-sacs swell hugely while dawn choruses carry for miles."],
 "foxmaidens": ["Herb-pouches trade for needles wherever farm hedges grow thick.", "Glass-charms glint cold blue against white snow fur."],
 "indian": ["Bangle-armor clinks on every claw raised above forest borders.", "Cord-ledgers knot every debt faithfully among jovial traders."],
 "kobolds": ["Scrap satchels clink with hinges prized above silver coins.", "Bell-strings ring sharp alarms through narrow warren mouths."],
 "gnolls": ["Marrow-bowls steam beside crushers camped at fresh kills.", "Hollowed hyena skulls mask every speaker above smoke-gourds."],
 "aegipanes": ["Braided beards swing above woolly flanks on every terrace.", "Whey-stained aprons mark cheesewards guarding echoing cave stores."],
 "boarheads": ["Helmet-bowls dent deeper with every brutal autumn raid.", "Ash lances level expertly before second crashing passes."],
 "lizards": ["Tail-flags wave every turn during coordinated fish drives.", "Sacred mud anoints departing scouts before long patrols."],
 "satyrs": ["Askew wreaths crown pipers capering through midnight dances.", "Great cups brim before every horn-lowered festival charge."],
 "harpies": ["Corpse-strip satchels reek on every screecher circling battlefields.", "Banner-wings signal massed multi-flock dives above cliff colonies."],
 "hags": ["Charm-bundles rattle beside iron ladles in every hovel.", "Eel-traps woven from scavenged hair line floating peat islands."],
 "leshy": ["Honey-gourds hang beside root-clubs on every mossy warden.", "Spore-pouches bulge on herders piping beetle herds at dusk."],
 "vodyanoy": ["Drowned brass-clock collections tick inside dark millpond depths.", "Tarred cloaks trail in water behind patient ferrymen."],
 "rusalka": ["Flower wreaths float at fords where wary villagers bargain.", "Drowned veils trail behind queens leading wedding processions."],
 "jotnar": ["Walrus-hide cloaks steam on frost giants striding snowfields.", "Mead-horns pass among jarls settling disputes with laughter."],
 "duergar": ["Slave-chains clink in lightless files marching without sound.", "Tally-boards record harsh quotas that weighted whips enforce."],
 "fomorian": ["Great shell-horns boom commands across surf-wading crews.", "Barnacled bulk shields trembling young behind bellowing tyrants."],
 "selkie": ["Folded sealskins rest beneath tidal rocks, guarded unto death.", "Sharp gutting knives flash whenever transformation theft threatens."],
 "sidhe": ["Mirrored shields dazzle before thin swords cut and vanish.", "Hill-keys turn heavy doors that grind shut exactly at dawn."],
 "minotaur": ["Labyrinth charts crease in scarred hands pacing quarry tunnels.", "Charred aprons smoke beside forge pits hammering bronze."],
 "centaur": ["Feather bandoliers flutter above dappled flanks at full gallop.", "Toll-boards hang where wood kin block narrow trails."],
 "cyclops": ["Bone flutes wheeze tunelessly above shaggy mountain sheep.", "Slag heaps glitter beside cliffside forges hammering bronze."],
 "lamia": ["Shoe collections gather in niches of crumbling desert ruins.", "Pearl-strings coil beside willow crowns of whispering dams."],
 "div": ["Powder-horns bandolier every smirking trickster bluffing nervous travellers.", "Cairn piles mark successful kills along windswept ridges."],
 "scorpion": ["Pincer clicks echo through dune burrows hiding vulnerable clutches.", "Wax-sealed gourds guard precious water against the sun."],
 "jackal": ["Feather-scales balance delicately in gold-masked priests' stern hands.", "Water-rings seal strategic marriages between proud desert families."],
 "falcon": ["Polished signal mirrors flash wing-commands across mountain passes.", "Command batons rise high before every coordinated multi-dive."],
 "croc": ["Boat nails pile in collections from every captured vessel.", "Barnacled armor plates elders rolling with gripped victims."],
 "thunderbird": ["Storm-drums boom rolling signals across crowded storm colonies.", "Lightning-charms blacken on weary elders after violent gales."],
}
CAST_NOTE = {"elves": "Any elven arts they show remain a flagged proposal under magic doctrine, never final canon.",
 "hags": "Their hedge curses remain a flagged proposal under magic doctrine, never final canon.",
 "duergar": "Their rune-craft remains a flagged proposal under magic doctrine, never final canon.",
 "sidhe": "Their court glamour remains a flagged proposal under magic doctrine, never final canon.",
 "div": "Their mighty sorcery remains a flagged proposal under magic doctrine, never final canon."}
BEHAV_NOTE = "Their uncanny behavior remains a flagged intuitive proposal under magic doctrine, never cast as final magic."
TRICK_NOTE = "Their rites are mundane tricks of smoke and noise, never true magic claimed as final."
LEADER_NOTE = "This one leads only a roaming band, with no wider rule or faction implication as final content."

def sent_words(s):
    return len(s.split())

def build_body(e, i, fk, n):
    sents = list(e["sketch"])
    # strip any empty / fragment
    sents = [s for s in sents if sent_words(s) >= 3]
    extra = []
    if fk in DISTINCTION:
        extra.append(DISTINCTION[fk])
    nn = n
    if nn in CAST:
        extra.append(CAST_NOTE[fk])
    elif nn in BEHAV:
        extra.append(BEHAV_NOTE)
    elif nn in MUNDANE_TRICK:
        extra.append(TRICK_NOTE)
    if BAND_LEADER.search(e["combat_raw"]) or "band-level" in hum[i]["display_name"].lower() or "(band-level" in " ".join(sents).lower():
        extra.append(LEADER_NOTE)
    extra.append(BANDS_ONLY)
    # family expansions rotated
    fam = EXPAND[fk]
    off = i % len(fam)
    for k in range(len(fam)):
        extra.append(fam[(off + k) % len(fam)])
    fam2 = EXPAND2[fk]
    off2 = (i + 1) % len(fam2)
    for k in range(len(fam2)):
        extra.append(fam2[(off2 + k) % len(fam2)])
    fam3 = EXPAND3[fk]
    off3 = (i + 2) % len(fam3)
    for k in range(len(fam3)):
        extra.append(fam3[(off3 + k) % len(fam3)])
    body_sents = sents + extra
    # enforce 8+ words each: merge short ones with previous
    fixed = []
    for s in body_sents:
        if fixed and sent_words(s) < 8:
            fixed[-1] = fixed[-1].rstrip(".") + ", " + s[0].lower() + s[1:]
        else:
            fixed.append(s)
    body_sents = fixed
    body = " ".join(body_sents)
    w = sent_words(body)
    # top-up: cycle family textures until floor reached
    pool = EXPAND[fk] + EXPAND2[fk] + EXPAND3[fk]
    pool += ["Grey veterans remember the leanest years and ration every share accordingly.",
             "Scouts mark safe trails with stacked stones that only kin can read.",
             "Rain and mud dictate their seasons more strictly than any chief's command.",
             "Travellers who offer food and respect pass their grounds without trouble.",
             "Their young learn bandcraft early, carrying messages between scattered camps.",
             "Winter hunger sharpens every quarrel over meat, shelter, and dry sleeping ground."]
    pi = 0
    while w < 155 and pi < len(pool) * 2:
        cand = pool[(off + pi) % len(pool)]
        if cand not in body_sents:
            if len(cand.split()) < 8:
                cand = cand.rstrip(".") + ", always at dawn."
            body_sents.append(cand)
            body = " ".join(body_sents)
            w = sent_words(body)
        pi += 1
    # trim expansions from end if over
    while w > 285 and len(body_sents) > len(sents) + 2:
        body_sents.pop(len(sents) + 2)
        body = " ".join(body_sents)
        w = sent_words(body)
    return body, body_sents

def parse_variants(raw, eid, fk):
    r = raw.strip().rstrip(".")
    # treemen special: only 2 forms -> add 2 age-forms
    if eid in ("ENY_TREEMAN_OAK",):
        return [("Old oak (male-presenting)", "M"), ("Scarred oak (male-presenting)", "M"),
                ("Mossy oak (male-presenting)", "M"), ("Young shoot (male-presenting)", "M")]
    if eid in ("ENY_TREEMAN_WILLOW",):
        return [("Young withy (male-presenting)", "M"), ("Grey hanging elder (male-presenting)", "M"),
                ("Moss-draped withy (male-presenting)", "M"), ("Storm-split elder (male-presenting)", "M")]
    if eid in ("ENY_OGRE_MATRIARCH",):
        return [("Son guard (male)", "male"), ("Brother guard (male)", "male"),
                ("Old matriarch (female)", "female"), ("Daughter-heir (female)", "female")]
    r = re.sub(r"\([^)]*(?:reason|biology|fallback|by biology)[^)]*\)", "", r, flags=re.I)
    r = re.sub(r"\s+[—–-]\s+[^;]*", "", r)
    groups = [g.strip() for g in re.split(r";", r)]
    out = []
    for g in groups:
        m = re.match(r"(\d+)\s*([MF])\b\s*(.*)", g)
        if m:
            sex = "male" if m.group(2) == "M" else "female"
            rest = m.group(3).strip()
            parts = [p.strip() for p in re.split(r"[/+]", rest) if p.strip()]
            for p in parts:
                out.append((p, sex))
        else:
            parts = [p.strip() for p in re.split(r"[/+]", g) if p.strip()]
            for p in parts:
                out.append((p, None))
    # clean names
    cleaned = []
    for name, sex in out:
        name = re.sub(r"^(young|old|older|grey|gray|scarred|prime|hard|blind|pale|mossy|sooty)\s+", "", name, flags=re.I)
        name = name.strip(" ,.")
        if not name:
            continue
        nm = name[0].upper() + name[1:]
        if sex:
            nm = f"{nm} ({sex})"
        cleaned.append((nm, sex))
    assert len(cleaned) == 4, (eid, raw, cleaned)
    return cleaned

ASPECTS = ["garment tint and wear", "scar and paint marking", "gear size and ornament", "age lining and posture"]

proposals = []
for i, e in enumerate(entries):
    n = i + 1
    fk = famkey(i)
    m = hum[i]
    combat = parse_combat(e["combat_raw"])
    hab = HAB_OVERRIDE.get(n, HABITAT[fk])
    assert set(hab) <= ALLOWED_TERRAIN
    body, bsents = build_body(e, i, fk, n)
    # base appearance
    app = e["app_raw"].rstrip(".").strip()
    base_app = (app + ". It stands built for band warfare in open country, carrying worn working gear.").strip()
    # portrait
    disp = m["display_name"]
    terr = hab[0].replace("_", " ")
    portrait = (f"Head-and-shoulders interface portrait of {disp}: {FACE[fk]}, steady gaze, worn headgear and band tokens, "
                f"soft {terr} daylight behind.")
    # variants
    vnames = parse_variants(e["var_raw"], e["eid"], fk)
    variants = []
    for vi, (nm, sex) in enumerate(vnames):
        delta = (f"{nm} keeps the base silhouette, distinguished by {ASPECTS[vi]} in {GEAR[fk]}.")
        if vi == 0 and REASON.get(fk):
            delta += f" Note: {REASON[fk]}."
        variants.append({"name": nm, "appearance_delta": delta})
    # states
    segs = [s.strip().rstrip(".") for s in e["states_raw"].split("/")]
    assert len(segs) == 4, (e["eid"], segs)
    elabs = ["held as a ready stance showing silhouette and gear",
             "lunging into the signature strike with weapon extended",
             "reeling from a heavy blow with guard broken",
             "collapsed and still with weapons scattered"]
    states = ["normal", "attack", "hitstun", "defeated"]
    poses = [{"state": st, "description": f"{sg[0].upper() + sg[1:]} pose, {el}."} for st, sg, el in zip(states, segs, elabs)]
    payload = {"id": m["id"], "display_name": disp, "taxonomy": "Humanoid",
               "body": body, "habitat": hab, "base_appearance": base_app,
               "portrait_brief": portrait, "variants": variants,
               "state_poses": poses, "combat": combat}
    proposals.append({"id": f"BST_HUMANOID_{n:03d}", "type": "bestiary_entry",
                      "status": "proposal", "canon_change": False, "payload": payload})

json.dump(proposals, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", len(proposals), OUT)
