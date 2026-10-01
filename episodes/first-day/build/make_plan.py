#!/usr/bin/env python3
"""Author the First Day pre-motion plan; local JSON/Markdown only, no API calls.

Rerunning writes only this episode's keyframes/timeline/motion manifests, shotlist,
and per-shot shot.md files. The source table below is the edit's authority.
"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[3]
EP = ROOT / "episodes/first-day"
BUILD = EP / "build"
FPS = 24
KEYS = {}
SECTIONS = []
STYLE = ("Photographic large-format film still in the approved porcelain maritime future, full 16:9. "
         "Preserve the base's architecture, materials, daylight direction and photographic finish. No extra people, text or interface.")
SKIN = "Keep the exact age and clear, even skin from the reference: add no blemishes, spots, weathering or extra lines."
CAST = {
    "lin": "Lin is the referenced 25-year-old Chinese woman, black chin-length bob, silver left-ear cuff, ivory high-neck sleeveless top, wide straight ivory trousers and flat ivory dance shoes.",
    "yu": "Yu is the referenced 27-year-old Chinese man, loose short black hair, clean-shaven, ink-blue collarless jacket over grey shirt, ink trousers and dark flat shoes."
}
LOC = {"a": "loc_a", "b": "loc_b", "i": "loc_i", "world": "world"}
EXTERNAL_REFERENCE_IDS = {"lin_base", "yu_base", "lin_costume", "yu_costume", "world",
                          "loc_a", "loc_b", "loc_i", "phase_model", "gate", "lin_sheet", "yu_sheet"}
def key(number, cast, location, camera, pose, action, *, kind="C", seconds=5, move="Locked companion camera.", extras=(), end=None, benchmark=False):
    identity = f"k{number:02d}"
    characters = [] if cast == "none" else [cast] if cast in CAST else ["lin", "yu"]
    KEYS[identity] = dict(id=identity, cast=characters, location=location, camera=camera, pose=pose,
                          action=action, category=kind, seconds=seconds, move=move,
                          extras=list(extras), end=end, benchmark=benchmark)


# Opening, the two halves of one phrase, and their separate places.
key(1,"lin","a","85 mm, camera 0.25 m high looking south along A's floor; ivory shoe left of centre.",
    "A supported white shoe is flat; the free right heel hovers just above pearl stone. Trouser hems remain separate; cobalt rail and ivory arch identify A behind.",
    "After a brief held preparation, Lin touches the free right heel to the floor once, transfers weight and settles.")
key(2,"yu","b","85 mm, camera 0.25 m high looking south along B's floor; dark shoe right of centre.",
    "Yu's supporting dark shoe is flat; the free left heel is prepared to land. Separated trouser hems; blue-grey floor and dark arch establish B.",
    "Yu answers with one grounded heel touch, weight transfer and settled feet.")
key(3,"lin","a","65 mm, chest-height 1.3 m, Lin left third with face and right hand clearly separated.",
    "Her right hand rests low beside her waist, palm angled toward screen right, poised to open. The cobalt rail is behind, never crossing wrist or face.",
    "Lin raises and opens her right palm toward screen right in one small invitation; her head remains level.")
key(4,"yu","b","65 mm, chest-height 1.3 m, Yu right third, clear face and left hand.",
    "His left hand is low and separate from his torso, ready to answer toward screen left. The slim dark arch remains visible at the frame edge.",
    "Yu opens his left palm toward screen left, gives one slightly too-early wrist settle, then lowers it.")
key(5,"both","i","Preserve the approved elevated oblique view across the bay, with all three separate spaces readable and distant human scale.",
    "Lin is on A at far left and Yu on B at far right, water gaps between both galleries and empty I. I has three silver ribs and its north public path. Rails, pylons and closed dock gates show support; nobody stands on I.",
    "A and B glide slowly on their separate visible guides past the fixed empty island; both people stay on their own decks.",seconds=6,
    move="A very short lateral drift preserves the approved elevated oblique angle and readable water gaps; no orbit.",extras=("loc_a","loc_b"))
key(6,"lin","a","50 mm, 1.4 m high, Lin left third, medium portrait with A's narrow arch at the right docking side.",
    "Her body faces the sea; her eyes rest toward screen right where Yu's gallery passes. Hands remain low; the profile is readable.",
    "Lin turns her eyes toward Yu and then briefly looks down; the head makes only a small natural adjustment.")
key(7,"yu","b","50 mm, 1.4 m high, Yu right third, waist-up with dark arch behind.",
    "He watches screen left with fingertips resting against his opposite sleeve cuff; the jacket remains unbuttoned and identical to reference.",
    "Yu straightens the sleeve cuff once, releases it and notices Lin across the water.")
key(8,"lin","a","50 mm, 1.2 m high, Lin left third beside A's cobalt glass rail; medium-full composition.",
    "One rain droplet lies on the dry rail cap. Her index finger stops a finger-width from it; her gaze rests on the droplet, body safely inside the rail.",
    "Lin lets her finger stop beside the droplet, then withdraws her hand and looks across to B.")
key(9,"yu","b","50 mm, 1.4 m high, Yu right third against the open sea and B's dark structural edge.",
    "His loose hair has one small wind-raised section; one hand remains below his shoulder before touching it.",
    "Yu smooths his hair once; the same mild sea breeze lifts it again after his hand drops.")
key(10,"lin","a","35 mm, 1.15 m high, full-body Lin left third, generous empty floor toward screen right.",
    "Lin begins balanced with soft knees, left foot supporting and free right heel close to the floor. Arms are separated and low. Ivory arch inland and cobalt sea rail stay in their approved positions.",
    "Lin performs one complete grounded phrase: right heel touch, quarter turn toward screen right, right palm opens, one small backward step, then settles fully on A.",seconds=7,benchmark=True)
key(11,"yu","b","35 mm, 1.15 m high, full-body Yu right third with travel space toward screen left.",
    "Yu begins balanced on his right foot, left heel prepared near the floor, arms low and separate. B's dark arch and coral inset remain fixed.",
    "Yu answers with left heel touch, a quarter turn toward screen left, an open left palm, then a backward step a fraction early; he settles on B.",seconds=7)
key(12,"lin","a","50 mm, 1.15 m high, full-body Lin left of centre, shoes well above the lower title-safe area.",
    "She is balanced just before a quarter turn: feet apart without crossed shins, right shoulder slightly leading, right hand low. A is the same approved set.",
    "Lin makes one grounded quarter turn, lets her right palm travel through a clear short arc and finishes balanced.")
key(13,"yu","b","50 mm, 1.15 m high, full-body Yu right of centre, clear floor toward screen left.",
    "He is balanced before the answering quarter turn, both feet supported and left arm separate from torso. Dark arch remains inland.",
    "Yu makes one grounded quarter turn toward Lin and settles with his left palm open.")
key(14,"lin","a","35 mm, 1.2 m high, full-body Lin left third, right palm and face separated in silhouette.",
    "Her right hand is offered at waist height toward screen right; feet are apart and securely supported before the familiar retreat. She remains far inside A's rails.",
    "Lin allows the offered right palm to register, then takes one modest backward dance step and settles; no dock crossing.")
key(15,"yu","b","35 mm, 1.2 m high, full-body Yu right third, left hand clear against blue water.",
    "His left palm begins open toward screen left, feet planted apart before a retreat; B's architecture is unchanged.",
    "Yu opens the left palm fully and takes one slightly too-early backward dance step within B, then settles.")
key(16,"lin","a","50 mm, 1.25 m high from north, full Lin at left docking threshold; empty I visible beyond right.",
    "A is stopped beside the left island dock, bridge level and gate open. Lin's two shoes remain entirely on A, behind the seam; right palm low. Empty island and three ribs are readable.",
    "Lin glances past the open level threshold toward departing B, begins to lift her right palm, then lowers it and stays entirely aboard A. Neither foot crosses the seam.",kind="A",seconds=7,extras=("loc_i","gate"))
key(17,"yu","b","50 mm, 1.25 m high from north, full Yu at right docking threshold; empty I beyond screen left.",
    "B is stationary at the right island dock, bridge level and gate open. Both of Yu's shoes remain on B behind the seam; he watches departing A rather than the clear floor.",
    "Yu begins to offer his left palm, watches A departing, withdraws the hand and remains entirely aboard B; no foot crosses the seam.",kind="A",seconds=7,extras=("loc_i","gate"))
key(18,"lin","a","65 mm, 0.55 m high, Lin's lower full body left of centre; knees and both shoes clear.",
    "Her weight is forward and the free foot is ready for one short backward dance step on the uninterrupted floor of A, away from its dock.",
    "Lin takes one short grounded backward step, then brings her weight over both feet; no jump or sliding foot.")
key(19,"yu","b","65 mm, 0.55 m high, Yu's lower body right of centre with knees and both shoes visible.",
    "The free foot is ready for one short backward dance step on B's blue-grey floor, well away from the docking threshold.",
    "Yu takes one short backward dance step slightly ahead of his hand settling, then finds a stable stance.")
key(20,"lin","a","35 mm, 1.15 m high, full Lin left third with clear lateral travel space and the ivory arch behind.",
    "She stands in a grounded lateral preparation, right foot free and hands separate; one shoulder points toward screen right without twisting the torso.",
    "Lin makes two buoyant grounded side steps to screen right, gives a compact quarter turn and comes back to a balanced stance.",seconds=6,
    move="Companion camera follows laterally just enough to keep her complete body and shoes in frame.")
key(21,"yu","b","35 mm, 1.15 m high, full Yu right third, clear floor to screen left and dark arch behind.",
    "He stands with relaxed knees before answering the two-step phrase, arms low and separate, jacket edge free of his hands.",
    "Yu answers with two buoyant grounded side steps toward screen left, a compact quarter turn and a settled finish.",seconds=6)
key(22,"lin","a","85 mm, 1.45 m high, Lin's face and upper torso left third, right shoulder foreground edge.",
    "Her eyes point to screen right, mouth closed, head quiet between phrases; the distant blue rail establishes A without busy detail.",
    "Lin lets her gaze follow Yu for a moment, then looks to the shared rhythm in her own hand; no mouth movement.")
key(23,"yu","b","85 mm, 1.45 m high, Yu's face and upper torso right third, dark arch as a clean background edge.",
    "His eyes point screen left, mouth closed; his head remains composed after the preceding dance phrase.",
    "Yu shifts his gaze to Lin and gives a small single chin adjustment, keeping his mouth closed.")
key(24,"both","i","Preserve the approved k05 elevated oblique geography, wide across A, empty I and B, with the same distant human scale.",
    "Lin remains on A at left and Yu on B at right. Both prepare complementary low open arms; water separates their floors from empty I. Gates are closed on passing galleries.",
    "Both perform a small answering arm phrase on their own supported gallery floors while the galleries pass the empty fixed island.",seconds=6,extras=("loc_a","loc_b"))
key(25,"lin","a","50 mm, 1.3 m high, Lin full at left and closed departure gate foreground edge, empty island receding right.",
    "Lin has stayed on A. Both feet are on its floor, hand lowered. Closed gate and broken water gap prove the opportunity has passed; nobody occupies I.",
    "A glides away from the island after the gate is closed; Lin stays still aboard, following the empty island with her eyes.",kind="A",seconds=6,extras=("loc_i","gate"))
key(26,"none","i","35 mm, 1.5 m high, fixed island's vacant central floor and sea beyond; three ribs at north edge.",
    "I is visibly empty, its public access path attached and both docks closed. One low bench sits outside the dance floor. The empty patch of pearl floor is the visual subject.",
    "The fixed island stays still while distant supported galleries continue slowly beyond it; the camera holds.",kind="D",seconds=5)
key(27,"yu","b","50 mm, 1.2 m high, Yu seated right third on B's dark bench with his complete legs and shoes visible.",
    "A jacket corner rests loose beside his thigh; one hand waits above it. Bench and dark arch are inland; the sea remains beyond the rail.",
    "Yu presses the wind-lifted jacket corner under his thigh once and leaves his hand on his knee.",seconds=7)
key(28,"lin","a","50 mm, 0.95 m high, seated Lin left third, both shoes and hands visible beside A's ivory bench.",
    "Her shoes are close together just above the floor; hands rest on the bench. She looks at the shoes before privately copying one fragment of Yu's premature retreat.",
    "Lin moves one shoe backward a few centimetres, notices the too-early beat, then places both shoes together; no display phrase.",seconds=6)
key(29,"lin","a","50 mm, 1.2 m high, seated Lin left third in three-quarter profile toward the sea.",
    "Her hands rest on the ivory bench beside her; the empty seat and sea horizon occupy the right half. Both feet have settled.",
    "Lin remains seated looking at the sea; near the end her eyes return toward B, with no other gesture.",kind="D",seconds=7)
key(30,"yu","b","50 mm, 1.2 m high, seated Yu right third in three-quarter profile toward the same sea horizon.",
    "His hands rest on his thighs, jacket corner contained; the vacant bench space is to his left. Same horizon and sun as Lin's matching view.",
    "Yu remains seated at the sea view, then turns his eyes toward A's approach without getting up.",kind="D",seconds=7)
key(31,"none","a","85 mm, 0.9 m high at tabletop eye level, the referenced small phase demonstration left of centre.",
    "The approved phase_model sits on A's fixed narrow console: a graded row of polished brass pendulums, each independently suspended, with unlabelled hardware. It is the only immaculate schematic object.",
    "The graded row of polished brass pendulums oscillates gently, each at its own differing period; no morphing, new pendulums or labels.",seconds=5,extras=("phase_model",))
key(32,"lin","a","50 mm, 1.25 m high, full standing Lin left third beside A's ivory bench, dock direction open to right.",
    "She has stood up; the right hand remains low, prepared for a very small invitation toward the island. Body and face stay composed.",
    "Lin makes the open-palm invitation smaller and more direct, indicating the island once, then leaves the hand low.",kind="A",seconds=6)
key(33,"yu","b","50 mm, 1.3 m high, Yu right third, torso and lowered hand visible with the right dock in depth.",
    "He has risen beside the dark bench and looks screen left toward Lin's new, smaller invitation. His left hand remains still.",
    "Yu notices Lin's small gesture and changes his gaze to the island while remaining in a stable full stance.",kind="A",seconds=5)
key(34,"none","b","85 mm, 0.8 m high, brass boarding-ribbon housing beside B's closed glass gate, no people.",
    "The complete referenced gate hardware is on B's blue-grey floor. A short coral boarding ribbon remains visibly outside its brass spool; no text, clock or numbers.",
    "The short physical boarding ribbon retracts once into its brass housing while the closed glass gate remains stationary.",seconds=5,extras=("gate",))
key(35,"both","i","Preserve the approved k05 elevated oblique geography and scale with all three decks, not a vertical drone map.",
    "A with Lin is stopped at the left island dock; B with Yu approaches at right on its different guide. I is still empty. Its public path, supports and both separate gate states are unmistakable.",
    "The elevated companion view holds long enough to read the offset arrivals; A remains stopped, B approaches, and both people remain aboard.",seconds=5,extras=("loc_a","loc_b"))
key(36,"lin","a","35 mm, 1.15 m high from north, full Lin left third at A's open dock, continuous bridge to I on the right.",
    "A is stationary and level with I. Lin's two feet are still wholly on A before the seam, facing right toward the clear bridge; three silver ribs identify I. Gate fully open, handrail uninterrupted.",
    "After a short preparation Lin walks across the stationary level left bridge once, in two ordinary steps, and stops with both feet fully on I. No retreat and no jump.",kind="A",seconds=5,end="k37",benchmark=True,extras=("loc_i","gate"))
key(37,"lin","i","35 mm, 1.15 m high from north, full Lin left of centre on I, the level left bridge behind her.",
    "Lin has completed the crossing: both ivory shoes wholly on fixed I beyond the seam, arms down, empty floor to her right. A remains stopped behind the open bridge; she is not straddling it.",
    "Lin finishes the last ordinary crossing step, places both feet securely on I, and keeps her body there.",kind="A",seconds=5,extras=("loc_a","gate"))
key(38,"lin","i","35 mm, 1.2 m high from north, full Lin left third on fixed I and a large empty right half.",
    "Both feet are planted well inside I and arms rest. The left gate is now closed before empty A departs behind her; A's ivory arch remains recognizable. Three ribs and the solid island floor prove stable ground.",
    "Lin stays planted on I without gesturing. Empty A glides slowly away behind the already closed left gate; no person or camera follows it.",kind="A",seconds=10,extras=("loc_a","gate"))
key(39,"yu","b","50 mm, 1.35 m high from north, Yu right third on B, island and waiting Lin's tiny ivory silhouette across left background.",
    "Yu stands with both feet aboard B and his hands still, looking left at the empty space beside Lin on I. His face is the focal point; the distant figure is only Lin, never a third person.",
    "Yu remains physically still as he notices Lin waiting on I; only his eyes settle on the space beside her.",kind="A",seconds=10,extras=("loc_i","lin_base"))
key(40,"lin","i","50 mm, 1.2 m high, full Lin left third on fixed I; open empty floor to screen right.",
    "Lin is balanced before her familiar phrase, right heel near the floor and right palm low. Her stopped stance on I and B's approaching right dock remain clear.",
    "Lin touches her heel, makes the familiar quarter turn and opens her right palm, but omits the backward step. Both feet remain on I as she waits.",kind="A",seconds=7)
key(41,"yu","b","35 mm, 1.15 m high from north, full Yu at screen right and open level bridge toward I at left.",
    "B is stopped at the right dock with gate fully open; both of Yu's shoes are still on B before the seam. Lin stands on I left background, right hand offered; four arms remain visually separate.",
    "Yu sees Lin's offered right hand, walks left across the stationary level bridge once and stops beside her on I, his left hand still separate before contact.",kind="A",seconds=8,end="k55",extras=("loc_i","lin_base","lin_costume","gate"))
key(42,"both","i","35 mm, 1.15 m high from north, uninterrupted full-body two-shot: Lin left, Yu right, four feet and both faces clear.",
    "Both now stand wholly on I with a small space between them. Lin's right palm and Yu's left hand are visibly separate before the first contact, arms comfortably bent. Three ribs behind; B is docked at right, closed to further boarding.",
    "The two share one complete grounded phrase: heel touch, quarter turn, Lin's right hand meets Yu's left once, a modest connected quarter turn, then balanced stillness together. Keep four feet, both faces and the joined hands visible throughout; no lifts or finger interlacing.",kind="A",seconds=10,end="k44",benchmark=True)
key(43,"both","i","50 mm, 1.2 m high from north, full-body Lin left and Yu right on one uninterrupted patch of I.",
    "Lin's right hand and Yu's left connect gently at waist height, no interlaced fingers. Both stand with separate supported feet, preparing one small grounded shared turn; no arms near faces.",
    "With one simple right-to-left hand connection they take two compact shared steps and settle on the same floor.",kind="A",seconds=7,end="k44")
key(44,"both","i","35 mm, 1.15 m high from north, same full two-shot and scale as the anticipatory duet frame.",
    "The modest shared turn has landed: Lin remains left and Yu right, both feet of each person fully supported, bodies angled slightly toward the sea, right-to-left hand connection relaxed at waist height. Exact I architecture and horizon.",
    "After the shared turn both hold a balanced finish, then ease their joined hands down without changing places.",kind="A",seconds=6)
key(45,"both","i","65 mm, 0.45 m high from north, four shoes and knees across one pearl-stone floor.",
    "Lin's ivory shoes occupy the left and Yu's dark shoes the right; all four have plausible support with a small shared dance gap. No crossed shins; no platform seam between them.",
    "Their four feet make one compact answering side-step pattern on the same stable floor, ending side by side.",seconds=5)
key(46,"both","i","85 mm, 1.05 m high from north, Lin's right hand at left meets Yu's left at right, shoulders outside the crop.",
    "One simple light hand connection at waist height, distinct wrists and fingers with no interlacing; Lin's bare forearm and ivory top edge identify the left person, Yu's ink sleeve the right. Pearl floor and silver rib softly behind.",
    "The single right-to-left hand connection gently opens and closes once as they adjust shared weight; preserve fingers and wrist anatomy.",kind="A",seconds=5)
key(47,"both","i","85 mm, 1.45 m high from north, Lin's face left third with Yu's ink shoulder at right edge.",
    "Lin looks toward the real person beside her rather than across water; composed mouth closed, bob and left cuff unchanged. The shared island ribs fix location.",
    "Lin looks at Yu beside her and then briefly follows their joined hand; her head and mouth remain quiet.")
key(48,"both","i","85 mm, 1.45 m high from north, Yu's face right third with Lin's ivory shoulder at left edge.",
    "Yu's eyes rest toward Lin beside him, face composed and mouth closed, with I's silver rib and blue sea behind.",
    "Yu looks toward Lin at his side and makes one small head adjustment, without performing for the camera.")
key(49,"both","i","35 mm, 1.2 m high from north, complete pair left and right on I with broad safe floor margins.",
    "They stand a comfortable arm's distance apart, connection released, both prepared for a playful answering side step. Feet and hands stay separate and readable.",
    "Lin offers two small side steps; Yu copies one slightly late, they adjust their spacing and arrive together on the next grounded step.",seconds=8)
key(50,"both","i","28 mm, 1.8 m high from north, full pair small but readable on I beneath the three silver ribs.",
    "Both stand on I after a shared phrase, hands lowered. Empty A and B depart on their visible guides; one spectacular open structural sweep frames the sea.",
    "The pair stays together on I as the empty galleries continue; the camera rises once to reveal the bay and their supported guide routes.",seconds=7,move="One motivated slow rise from 1.8 to 4 metres; no orbit or simultaneous zoom.",extras=("loc_a","loc_b"))
key(51,"both","i","35 mm, 1.2 m high from north, full pair in the central floor moving toward the south sea rail.",
    "Lin left and Yu right face the sea at a slight angle, ready to walk side by side; hands hang naturally and no dance pose remains. A clear pedestrian route leads to the rail.",
    "They take three ordinary side-by-side steps toward the sea railing, then stop safely inside it; no bench or sitting.",seconds=7)
key(52,"both","i","50 mm, 1.3 m high from north-northeast, full pair at the sea rail; three-quarter profiles retain natural faces.",
    "Both stand upright near each other, Lin left and Yu right. His left hand rests low between them, fingers naturally relaxed before the palm opens; her right arm is relaxed. They face the same sea, feet planted.",
    "During the first four seconds Yu opens his left palm once and Lin moves one small step beside him. By 4.5 seconds both have settled; they then stay standing sea-facing without another hand gesture or step for the remainder of the take.",seconds=10)
key(53,"both","i","85 mm, 0.25 m high from north, ivory and dark shoes together on the same uninterrupted pearl floor.",
    "Both pairs of shoes are at rest, ivory left and dark right, with a comfortable small gap; four feet fully supported. A thin cobalt reflection comes from the visible railing edge above.",
    "Both people settle their weight on the same floor and keep their shoes still; no dance restart.",kind="D",seconds=6)
key(54,"both","i","28 mm, 1.6 m high from north, wide final tableau with the standing pair at the south rail and open sea filling the upper half.",
    "Lin and Yu stand side by side, seen in quiet three-quarter rear profile, ivory left and ink right, full bodies and shoes clear. The three silver ribs in the foreground and empty departing galleries preserve the exact established world; no one sits.",
    "They remain standing sea-facing, bodies quiet; the mild sea breeze moves only hair and a jacket edge while galleries continue in the distance.",kind="D",seconds=10,extras=("loc_a","loc_b"))
key(55,"both","i","50 mm, 1.3 m high from north, full Lin at left and newly arrived Yu at right with open right dock behind.",
    "Yu has just completed his crossing: both dark shoes wholly on I beyond the right seam; both ivory shoes already on I. Lin's right hand and Yu's left remain separate. B is stopped, bridge level and gate still open; this is arrival, before the first shared dance.",
    "Yu finishes his final ordinary step onto I, stops at a natural distance from Lin, and leaves his left hand visibly separate before their first contact.",kind="A",seconds=5,extras=("loc_b","gate"))


def configure_image_recipes():
    """Use approved scene compositions, then apply exact director-approved recipes.

    Portraits remain identity references. They do not supply the canvas for a
    distant dancer. Guides are completed assets, not unreviewed generated chains.
    """
    override_path = BUILD / "approved_image_overrides.json"
    overrides = json.loads(override_path.read_text())
    if isinstance(overrides, dict) and "overrides" in overrides:
        overrides = overrides["overrides"]
    if isinstance(overrides, list):
        if len({item["id"] for item in overrides}) != len(overrides):
            raise ValueError("Duplicate approved override IDs")
        overrides = {item["id"]: {k: v for k, v in item.items() if k != "id"} for item in overrides}
    if not isinstance(overrides, dict) or set(overrides) - KEYS.keys():
        raise ValueError("Approved image overrides must map known keyframe IDs to recipes")
    if {"k05", "k10", "k42"} - overrides.keys():
        raise ValueError("The approved k05, k10 and k42 composition guides must be recorded first")

    routes = {}

    def route(numbers, base, refs, framing, *, face=True, camera=True):
        for number in numbers:
            identity = f"k{number:02d}"
            if identity in routes:
                raise ValueError(f"Duplicate composition route: {identity}")
            routes[identity] = (base, refs, framing, face, camera)

    # k10 is already a complete, approved A scene: retain its wide floor and
    # wardrobe rather than adding competing costume or location pictures.
    route([12,14,20,32], "k10", ["lin_base"],
          "Keep the approved base's exact wide framing, figure scale, floor margins and wardrobe. Change only Lin's pose as follows. She looks toward screen right, never left.", camera=False)
    route([16,25,36], "k10", ["lin_base", "loc_i"],
          "Keep Lin as small as in the approved base with the same deep floor margin. Show the docking connection at screen right; change only her pose and the specified docking state. The island reference governs only the island beyond A.")
    route([28,29], "k10", ["lin_base"],
          "Keep the approved base's wide view, deep floor margin and existing bench at far left. Change only Lin's position to seated on that bench and the described small pose; retain her complete shoes.", camera=False)
    route([3,6,8], "k10", ["lin_base"],
          "Reframe the approved A scene to the described medium composition, keeping Lin left and her attention toward screen right. The ivory arch belongs at the right docking side; preserve the skyline on the left.")
    route([22], "lin_base", ["loc_a"],
          "Close portrait of the original Lin identity in A. Face and upper torso only; gaze toward screen right. Do not invent a new face or change the actual local set.")
    route([1,18], "k10", [],
          "Reframe downward into a low shoe-and-trouser detail of the approved Lin scene. Exclude the head and upper torso; show only the specified legs, shoes and their floor contact.", face=False)

    # B has no approved dancer-wide guide. Its architecture is the canvas;
    # original Yu and costume references supply the person without portrait scale.
    route([11,13,15,21,27,30], "loc_b", ["yu_base", "yu_costume"],
          "Wide B scene: one small complete Yu at the right third. Head-to-shoe height at most half the image; leave the bottom quarter clear floor and ample space to screen left. Preserve B's existing floor, dark arch, bench and coral inset.")
    route([17], "loc_b", ["yu_base", "yu_costume", "loc_i"],
          "Wide right-dock view: Yu is small at screen right, with complete shoes above a deep clear floor margin. B occupies the right and fixed I the left. Show one unambiguous level transfer seam and its specified gate state.")
    route([4,7,9,33], "loc_b", ["yu_base", "yu_costume"],
          "One Yu at the right third of the approved B scene, in the described torso-and-hand framing. His attention is toward screen left. Preserve the local dark arch and coral inset; do not enlarge him into a foreground head crop.")
    route([23], "yu_base", ["loc_b"],
          "Close portrait of the original Yu identity in B. Face and upper torso only; gaze toward screen left. Preserve his youthful clear skin and the local dark architectural edge.")
    route([2,19], "loc_b", ["yu_costume"],
          "Low close detail on B's blue-grey floor: only Yu's ink trouser legs and dark flat shoes. Exclude head, torso and hands. Both shoes remain fully inside the crop.", face=False)

    # Empty-island and separated-gallery pictures never use the duet base.
    route([24,35], "k05", [],
          "Keep the base's wide oblique geography, distant human scale and exact deck identities. Change only the specified poses and docking state. Lin stays on A at left, Yu on B at right; the central island stays empty.", face=False, camera=False)
    route([26], "loc_i", [],
          "Preserve the approved island view with no people anywhere. The vacant central pearl floor is the subject. Change only the specified gate state.", face=False)
    route([31], "phase_model", ["loc_a"],
          "Close tabletop view of the exact approved physical phase model, all bobs retained. Only its quiet A-gallery setting changes; no person or body in frame.", face=False)
    route([34], "gate", ["loc_b"],
          "Close object detail of the complete approved ribbon-reel housing beside B's glass gate, with a short ribbon still outside. No people. Keep this crop about the mechanism, not a wide dock view.", face=False)
    route([37,38], "loc_i", ["lin_base", "lin_costume", "loc_a"],
          "Wide island view: add only Lin on the left third, complete head-to-shoe height at most half the image and bottom quarter clear floor. Yu is absent. Preserve I; the A reference governs only the left background deck and its specified dock state.")
    route([40], "loc_i", ["lin_base", "lin_costume", "loc_b"],
          "Wide island view: add only Lin on the left third, complete head-to-shoe height at most half the image and bottom quarter clear floor. Keep the right half empty beside her; Yu remains off this island. B is only the approaching right background gallery.")
    route([39], "loc_b", ["yu_base", "yu_costume", "loc_i", "lin_base"],
          "Yu stands still on B at screen right, looking left. Compose his face and torso clearly while showing distant I at left with only a tiny ivory-clad Lin; no third person. The island reference governs the background, not his floor.")
    route([41], "loc_i", ["yu_base", "yu_costume", "lin_base", "lin_costume", "loc_b"],
          "Wide level right-dock view: Yu stands wholly on B at screen right before its seam; Lin stands wholly on I at left. Both are small complete figures above a deep floor margin. B's reference governs the right gallery; preserve one clear open level bridge, not overlapping floors.")

    # The successful duet supplies scale, clothing and separation. Original
    # portraits are still the identity authorities; no repeated edit chain.
    route([43,44,49], "k42", ["lin_base", "yu_base"],
          "Keep the approved duet base's exact wide framing, figure sizes, costumes and deep floor margin. Change only the specified body/hand pose. Lin stays left, Yu right, four shoes fully visible.", camera=False)
    route([51,52], "k42", ["lin_base", "yu_base"],
          "Keep the approved duet's wide framing, figure scale, costumes and deep floor margin. Change only their position/orientation as described toward the existing sea rail; both remain standing with four shoes visible.", camera=False)
    route([55], "k42", ["lin_base", "yu_base", "loc_b"],
          "Keep the approved duet's wide framing, figure scale, costumes and deep floor margin. Change only the arrival pose and right docking state: B remains docked with its gate open; the hands have not met.", camera=False)
    route([50,54], "k42", ["lin_base", "yu_base", "world"],
          "Open the approved duet view into the described wider geography, keeping both people small, complete and safely on I. Preserve the island foreground and wardrobe; the world reference governs only the separate empty departing galleries and distant supported routes.")
    route([45,53], "k42", [],
          "Reframe downward from the approved duet into the described four-shoe detail. Exclude heads, torsos and hands; retain ivory shoes at left, dark shoes at right on one continuous pearl floor.", face=False)
    route([46], "k42", [],
          "Reframe the approved duet into a close waist-height hand detail, shoulders and faces outside the crop. Only Lin's bare right forearm from left and Yu's ink-sleeved left forearm from right form the specified light connection.", face=False)
    route([47,48], "k42", ["lin_base", "yu_base"],
          "Reframe the approved duet into the described close face and partner-shoulder composition. Preserve the original identity references and the pair's left/right order; no full-body framing is requested.")
    if set(routes) | set(overrides) != KEYS.keys():
        raise ValueError(f"Missing composition routes: {KEYS.keys() - (set(routes) | set(overrides))}")

    for identity, source in KEYS.items():
        if identity in routes:
            base, refs, framing, face, use_camera = routes[identity]
            # Remove obsolete verbal arch placement; the approved A picture
            # puts the narrow arch at its right docking side.
            camera = source["camera"].replace("A's arch at left edge", "A's narrow arch at the right docking side")
            descriptions = [CAST[p] for p in source["cast"]] if face and base.startswith("loc_") else []
            prompt = " ".join(filter(None, [framing, camera if use_camera else "", source["pose"],
                                           *descriptions, STYLE,
                                           "Faces composed, mouths closed. Original portraits govern identity. " + SKIN if face and source["cast"] else ""]))
            source.update(mode="edit", base=base, refs=refs, prompt=prompt,
                          scene_model="luma/agent/uni-1/v1/max/edit", external=False)
        if identity in overrides:
            override = overrides[identity]
            for field in ("mode", "base", "refs", "prompt", "scene_model", "external"):
                if field in override:
                    source[field] = override[field]
            source["override_metadata"] = {k: v for k, v in override.items() if k not in {"mode", "base", "refs", "prompt", "scene_model", "external"}}
            source.setdefault("external", False)
        for field in ("mode", "refs", "prompt", "scene_model"):
            if field not in source:
                raise ValueError(f"{identity}: approved recipe missing {field}")
        if source["mode"] not in {"t2i", "edit"}:
            raise ValueError(f"{identity}: unsupported image mode")
        if source["mode"] == "edit" and not source.get("base"):
            raise ValueError(f"{identity}: edit recipe needs a base")
        source["refs"] = list(dict.fromkeys(source["refs"]))
        if len(source["refs"]) > 8 or "yu_sheet" in source["refs"]:
            raise ValueError(f"{identity}: invalid reference set")
        source["sheet_note"] = ("Original portraits govern faces; approved scene bases govern composition. "
                                "Yu's sheet remains excluded after age/skin drift. "
                                "Lin's sheet is supporting evidence only and is omitted where the approved scene already fixes the angle.")
        if not source["cast"] or identity in {"k01", "k02", "k18", "k19", "k45", "k46", "k53"}:
            source["sheet_note"] = "No visible face requires portrait or sheet conditioning in this detail/location image."
        elif identity in {"k05", "k24", "k35"}:
            source["sheet_note"] = "Tiny geography figures preserve the approved frame's people and wardrobe; no readable facial-detail claim."
        elif source["external"]:
            source["sheet_note"] = "External approved image recipe records its identity and composition inputs; original portraits remain face authorities."

    available = EXTERNAL_REFERENCE_IDS | KEYS.keys()
    visiting, visited = set(), set()

    def verify(identity):
        if identity in visiting:
            raise ValueError(f"Cyclic image dependency: {identity}")
        if identity in visited:
            return
        visiting.add(identity)
        source = KEYS[identity]
        deps = set(source["refs"]) | ({source["base"]} if source.get("base") else set())
        if deps - available:
            raise ValueError(f"{identity}: unresolved image dependencies {deps - available}")
        for dep in deps & KEYS.keys():
            verify(dep)
        visiting.remove(identity)
        visited.add(identity)

    for identity in KEYS:
        verify(identity)


def section(label, end, entries):
    """entries = (key, relative length, kind, cut purpose). Lengths allocate whole frames."""
    SECTIONS.append((label, end, entries))


# Edit rows follow below; preserved song boundaries quantize upward to whole frames.
section("opening",611,[
 (1,1.25,"dance","Ivory heel begins the borrowed beat."),(2,1.25,"dance","Dark heel completes her step across the cut."),
 (3,1.5,"dance","Her palm initiates an unfinished offer."),(4,1.5,"dance","His palm completes the visual sentence."),
 (5,5,"geography","Reveal separate galleries, empty island, safe public path and visible supports."),
 (6,3,"story","Lin notices that the answer belongs to a real stranger."),(7,3,"story","Yu makes the sleeve adjustment she sees."),
 (1,2,"dance","A second heel tap establishes invitation by repetition."),(2,2,"dance","His matching heel responds, still on B."),
 (6,4.46,"story","Her quiet attention leaves sky for the opening title.")])
section("verse_one",1411,[
 (8,4.6,"story","A droplet arrests Lin's hand before her eyes seek Yu."),(9,4.6,"story","His hair defeats one careful adjustment."),
 (10,4.8,"dance","First readable Lin phrase: heel, quarter turn, palm, retreat."),
 (11,4.8,"dance","Yu echoes the phrase but retreats a fraction early."),
 (6,3,"story","She looks away before privately accepting the game."),
 (32,3.8,"story","Lin indicates the island with one small offered palm."),
 (33,3.8,"story","Yu notices the suggested destination without approaching yet."),
 (14,3.97,"dance","Her open palm becomes the dance's next invitation.")])
section("chorus_one",2249,[
 (20,4.5,"dance","A sustained full-body phrase gives the fast details physical weight."),
 (21,3.5,"dance","His answering full-body phrase moves toward her screen direction."),
 (1,.8,"dance","Heel accent A."),(2,.8,"dance","Matching heel accent B."),
 (12,1.1,"dance","Lin's quarter-turn starts the directional match."),(13,1.1,"dance","Yu's turn completes it across distance."),
 (3,.7,"dance","Her open palm punctuates the phrase."),(4,.7,"dance","His hand answers before the next footstep."),
 (18,.8,"dance","Her backward step remains safely on A."),(19,.8,"dance","His retreat lands a fraction early on B."),
 (22,1,"story","See the person whose movement we borrowed."),(23,1,"story","His reciprocal gaze makes the editing relational."),
 (14,1.3,"dance","Refrain: offered hand retains the same direction."),(15,1.3,"dance","Refrain: answering palm retains its owner."),
 (20,1.2,"dance","A later phrase fragment repeats the lateral travel."),(21,1.2,"dance","The separate full bodies form an apparent pair."),
 (24,2.2,"dance","Wide admits the water gap while both answer."),
 (12,1,"dance","One last quarter-turn before the opportunity."),(13,1,"dance","His answer passes away with B."),
 (16,3.2,"story","First missed connection: Lin hesitates with both feet aboard stopped A."),
 (25,2.4,"story","Gate closed, A leaves with her still aboard."),(26,2.4,"story","The empty island is the consequence, not landscape filler.")])
section("verse_two",3046,[
 (27,5.5,"story","Wind lifts the jacket edge; Yu secures it under his thigh."),
 (28,4.5,"gesture","Lin privately tries one fragment of his premature step, then stops."),
 (29,4.7,"story","Her sea view includes the empty half of her own bench."),
 (30,4.7,"story","His matching sea view has its own empty space; they are still separate."),
 (31,3.2,"object","One physical phase-model insert echoes the asynchronous arrivals."),
 (32,3.8,"story","Lin stands and pares the invitation down."),(33,3.8,"story","Yu follows the small gesture to the island."),
 (9,3,"story","The imperfect hair returns as a personal detail, not another display phrase.")])
section("chorus_two",3840,[
 (11,4.2,"dance","Yu's complete answer grows more urgent while camera stays put."),
 (10,3.6,"dance","Lin continues the familiar phrase instead of introducing new tricks."),
 (19,.9,"dance","His early retreat returns."),(18,.9,"dance","Her matching retreat answers within A."),
 (15,1.1,"dance","Yu almost leaves the invitation open."),(14,1.1,"dance","Lin's palm passes him on the other gallery."),
 (17,3.6,"story","Second missed connection: Yu withdraws his palm and stays on B."),
 (34,1.2,"object","Physical boarding ribbon retracts; this local pass is ending."),
 (23,1,"story","Yu watches A leave."),(22,1,"story","Lin sees his hesitation repeat hers."),
 (1,.8,"dance","Ivory heel answers the echoed lyric."),(2,.8,"dance","Dark heel repeats it."),
 (12,1.1,"dance","Quarter-turn A, clear feet."),(13,1.1,"dance","Quarter-turn B, equal direction."),
 (3,.7,"dance","Open right palm A."),(4,.7,"dance","Open left palm B."),
 (20,1.7,"dance","Lin gives the last separate lateral answer."),(21,1.7,"dance","Yu replies without advancing to a dock."),
 (35,2.5,"geography","Single elevated view explains the offset arrivals and empty island."),
 (16,1.4,"story","At A's next stopped dock, Lin prepares; both shoes remain aboard until 160 seconds.")])
section("lin_crosses",3936,[
 (36,2.3,"story","At 160 seconds Lin begins her only crossing across the level left bridge."),
 (37,1.7,"story","By 164 seconds both of Lin's feet have landed on I, with no retreat.")])
section("waiting",4300,[
 (38,7.58,"stillness","Hard stop: Lin and camera stay on I while empty A leaves behind its closed gate."),
 (39,7.58,"stillness","Yu and camera stay still; his sight of the empty space beside Lin supplies the answer's cause.")])
section("yu_answers",4586,[
 (40,3,"dance","Heel, quarter turn, palm: Lin deliberately omits the backward step."),
 (39,1.8,"story","Yu sees the invitation from B; do not cut directly from a hand to an unexplained arrival."),
 (41,3.7,"story","Yu crosses once from stopped B through the right level dock."),
 (55,3.42,"story","Both are now wholly on I; separate hands establish the moment before real contact.")])
section("final_chorus",5354,[
 (42,7.5,"dance","First uninterrupted proof: complete familiar phrase, real hand contact, modest shared turn, four feet visible."),
 (44,1.2,"dance","Balanced landing is the consequence of that shared turn."),
 (45,.8,"dance","Four feet now answer on one floor."),(46,.8,"dance","One unambiguous right-to-left hand connection."),
 (47,1,"story","Lin looks beside her instead of across water."),(48,1,"story","Yu answers at the same physical distance."),
 (43,2,"dance","Another complete short partnered phrase keeps contact modest."),
 (49,3,"dance","The small late step becomes a playful shared adjustment."),
 (45,.8,"dance","They recover to the same next step."),(46,.8,"dance","Joined hands respond to ordinary shared weight."),
 (49,1.4,"dance","A fresh fragment from the play phrase, no new acrobatic vocabulary."),
 (43,1.5,"dance","Familiar offer now has a real receiver."),(44,1.6,"dance","They settle together instead of retreating apart."),
 (47,1,"story","Her attention belongs to the person beside her."),(48,1,"story","His restrained answer leaves the body as the performance."),
 (50,5,"geography","One earned rising view: the pair stays as both galleries continue.")])
section("coda",6096,[
 (49,2.4,"dance","A last playful phrase echoes the English refrain."),(45,1.5,"dance","Shared floor replaces the opening's borrowed footstep."),
 (46,1.5,"dance","The hand connection loosens naturally."),(44,1.8,"dance","Last balanced dance finish; no virtuoso escalation."),
 (51,4.4,"story","Ordinary walking carries them toward the sea rail."),
 (52,4.4,"story","Yu opens his hand once; Lin comes to stand beside him."),
 (53,3.7,"stillness","Opening shoe composition returns with both pairs resting on one floor."),
 (52,3.2,"stillness","Both remain upright and sea-facing; no sitting or obligatory kiss."),
 (54,8,"stillness","Final standing wide carries the complete song tail; credits after the last lyric.")])


def allocate(weights, total):
    raw = [weight / sum(weights) * total for weight in weights]
    counts = [math.floor(v) for v in raw]
    order = sorted(range(len(raw)), key=lambda i: (raw[i] - counts[i], -i), reverse=True)
    for i in order[:total - sum(counts)]:
        counts[i] += 1
    assert sum(counts) == total and min(counts) > 0
    return counts


def write_json(target, value):
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(target)


def timecode(frame):
    return f"{frame // (FPS*60):02}:{frame // FPS % 60:02}:{frame % FPS:02}"


def main():
    configure_image_recipes()
    timeline, cursor = [], 0
    for label, end, rows in SECTIONS:
        counts = allocate([row[1] for row in rows], end - cursor)
        for (number, _, kind, purpose), count in zip(rows, counts):
            key_id = f"k{number:02d}"
            source = KEYS[key_id]
            identity = f"{len(timeline)+1:02d}"
            action = source["action"]
            # This is anticipation only: never let the reused hesitation source cross early.
            if label == "chorus_two" and key_id == "k16":
                action = "Lin stands behind A's seam with both feet aboard at the open stopped dock, preparing to cross only when the next shot begins at 160 seconds."
            group = "m36" if key_id == "k37" else "m41" if key_id == "k55" else "m" + key_id[1:]
            occurrence = sum(s["motion_job"] == group for s in timeline)
            if label == "coda" and key_id == "k52" and occurrence > 0:
                action = "Both remain standing sea-facing after the completed invitation and step; neither repeats a hand gesture or takes another step."
            duration = count / FPS
            nominal = KEYS["k" + group[1:]]["seconds"]
            head = min(.5 + occurrence * .35, max(0, nominal - duration - .2))
            if label == "lin_crosses":
                head = .5 if key_id == "k36" else .5 + timeline[-1]["duration"]
            if label == "yu_answers" and key_id == "k41":
                head = .5
            if label == "yu_answers" and key_id == "k55":
                head = .5 + timeline[-1]["duration"]
            if label == "final_chorus" and key_id == "k42":
                head = .5
            if label == "coda" and key_id == "k52" and occurrence > 0:
                head = 6.0
            assert head + duration <= nominal + 1e-6, (identity, group, head, duration, nominal)
            entry = dict(id=identity, start_frame=cursor, end_frame=cursor+count,
                         image=f"episodes/first-day/assets/keyframes/{key_id}.png", keyframe_id=key_id,
                         section=label, kind=kind, duration=duration, action=action, purpose=purpose,
                         camera=source["move"], cut="hard cut; held startframe in pre-motion reel",
                         motion_job=group, source_trim={"start":round(head,6),"end":round(head+duration,6),"status":"provisional; replace with observed usable action timestamps"},
                         occupancy=("Lin on I; Yu aboard B" if label == "waiting" else "Lin and Yu on I" if label in ("final_chorus","coda") else "see action and docking state"),
                         action_qa={"status":"pending generated footage and playback", "required_action":action,
                                    "required_count":1,"source_onset_seconds":None,"source_completion_seconds":None,
                                    "full_take_verified":False,"final_cut_verified":False,"reviewer":None})
            timeline.append(entry)
            cursor += count
    assert cursor == 6096 and 90 <= len(timeline) <= 110 and len(KEYS) <= 58
    assert all(a["end_frame"] == b["start_frame"] for a,b in zip(timeline,timeline[1:]))
    assert not any(s["section"] == "waiting" and "Locked" not in s["camera"] for s in timeline)
    dance_frames = sum(s["end_frame"]-s["start_frame"] for s in timeline if s["kind"] == "dance")
    assert .4 <= dance_frames / cursor <= .5, dance_frames / cursor
    first_duet = next(s for s in timeline if s["section"] == "final_chorus")
    assert 7 <= first_duet["duration"] <= 8
    images = []
    for key_id, source in KEYS.items():
        item = {"id":key_id,"out":f"episodes/first-day/assets/keyframes/{key_id}.png","mode":source["mode"],
                       "refs":source["refs"],"deps":list(dict.fromkeys(([source["base"]] if source.get("base") else [])+source["refs"])),
                       "prompt":source["prompt"],"aspect":"16:9","shots":[s["id"] for s in timeline if s["keyframe_id"]==key_id],
                       "scene_model":source["scene_model"],"external":source["external"],"location":source["location"],
                       "character_sheet_note":source["sheet_note"],"approval":"pending generation and visual QA"}
        if source.get("base"):
            item["base"] = source["base"]
        item.update(source.get("override_metadata", {}))
        images.append(item)
    jobs = []
    for key_id, source in KEYS.items():
        identity = "m"+key_id[1:]
        uses = [s for s in timeline if s["motion_job"] == identity]
        if not uses:
            continue
        motion_prompt = ("Photoreal cinematic image in the established porcelain maritime future. " + source["camera"] + " " + source["action"] +
                         " Preserve the supplied identities, age, costumes, supported architecture and closed/open dock state. "
                         "Understated facial performance: mouths closed; only the described body movements happen. " + source["move"] +
                         " No generated text or lip movements. Diegetic sound only; no music. Return audio will be discarded.")
        job = {"id":identity,"image":f"episodes/first-day/assets/keyframes/{key_id}.png","prompt":motion_prompt,
               "duration":source["seconds"],"out":f"work/first-day/motion/{identity}.mp4","deps":[],
               "category":source["category"],"planned_takes":2 if source["category"]=="A" else 1,
               "reference_ids":source["refs"],"image_key":key_id,"benchmark":source["benchmark"],
               "source_trims":[{"shot":s["id"],**s["source_trim"]} for s in uses],
               "action_qa":{"status":"pending; prompt is direction, not verification","required_action":source["action"],
                            "source_onset_seconds":None,"source_completion_seconds":None,"full_take_verified":False,"final_cut_verified":False},
               "submission_status":"NOT SUBMITTED; motion stage requires approval after estimate"}
        if source["end"]:
            job["end_image"] = f"episodes/first-day/assets/keyframes/{source['end']}.png"
            job["end_image_key"] = source["end"]
        jobs.append(job)
    motion = {"defaults":{"endpoint":"i2v","resolution":"768P","prompt_expansion_mode":"disabled"},
              "stage":"prepared only; no requests submitted","root":"repository root; pass --root explicitly",
              "benchmark_ids":[j["id"] for j in jobs if j["benchmark"]],"fps":FPS,"planned_edit_frames":cursor,
              "estimated_primary_seconds":sum(j["duration"] for j in jobs),
              "estimate_basis":"Use current primary pricing before approval. Historical H3 Max guide: $0.025/second; takes/retakes add spend.",
              "estimated_seconds_with_planned_takes":sum(j["duration"]*j["planned_takes"] for j in jobs),
              "unused_model_audio":"discard every model-returned audio track; use the locked supplied-song master",
              "jobs":jobs}
    write_json(BUILD/"keyframes.json",images)
    write_json(BUILD/"timeline.json",timeline)
    write_json(BUILD/"motion_plan.json",motion)
    by_job = {j["id"]:j for j in jobs}
    for shot in timeline:
        source = KEYS[shot["keyframe_id"]]
        job = by_job[shot["motion_job"]]
        directory = EP/"shots"/shot["id"]
        directory.mkdir(parents=True,exist_ok=True)
        body = f"""# Shot {shot['id']} — {shot['section']}

- Edit: **{timecode(shot['start_frame'])}–{timecode(shot['end_frame'])}**, end-exclusive frames {shot['start_frame']}–{shot['end_frame']}, {shot['duration']:.3f} s at 24 fps.
- Kind: {shot['kind']}. Purpose: {shot['purpose']}
- Source keyframe: `{shot['image']}` ({shot['keyframe_id']}); shared source reuse is intentional where the phrase recurs.
- Image composition base: `{source.get('base') or 'external approved asset; see recorded recipe'}`. Scene model: {source['scene_model']}.
- Identity/location references: {', '.join('`'+r+'`' for r in source['refs'])}.
- Character-sheet coverage: {source['sheet_note']}
- Camera owner: companion view within the approved setting; geography shots retain their established elevated oblique angle. Planned camera: {shot['camera']}
- Pre-motion treatment: {shot['cut']}. No synthetic footwork, camera pan, zoom or pose interpolation.
- Visible action: {shot['action']}
- Relationship to other event: {shot['purpose']}
- Light: preserve the approved composition/local reference's daylight direction and shadows; the oblique A view is not the common south-facing angle.
- Audio: uninterrupted locked source song; no new voice and no model-returned audio.

## Exact image prompt

{source['prompt']}

## Future motion job

`{shot['motion_job']}` in `episodes/first-day/build/motion_plan.json`; image `{job['image']}`; {job['duration']} s, 768P, H3 Max, prompt expansion disabled. Category {job['category']}. End pose: {job.get('end_image','none required')}.

{job['prompt']}

Planned source trim: {shot['source_trim']['start']:.3f}–{shot['source_trim']['end']:.3f} s. This is provisional. Locate the actual action before choosing the trim; a late usable event may require a new edit rather than cutting it away.

## Required action QA — pending

- Required count: one specified event or phrase; preserve its internal order.
- Full-take onset: **pending**. Full-take completion: **pending**.
- Full-take action/order/contact/weight verified: **no**.
- Final cut retains the complete required event: **not checked**.
- Check faces, mouth closure, feet, hand anatomy, costume, support, dock state, screen direction, sunlight and neighboring-shot geography.
- Check Lin remains aboard before frame 3840, is fully on I by frame 3936, and never returns to A. Yu crosses only in the 4300–4586 answer section. Both end standing sea-facing.
- Motion, lyric synchronization and musical timing require playback review. The stills reel supplies no motion-quality pass.
"""
        (directory/"shot.md").write_text(body)
    intro = (f"# 第一天 — shot list\n\n{len(timeline)} edited shots; {len(images)} generated keyframes; 6096 frames / 254.000 s at 24 fps, including the 40 ms picture tail after the complete 253.960 s recording.\n\n"
             f"Dance-designated screen time: {dance_frames/FPS:.3f} s ({dance_frames/cursor:.1%}). Pre-motion output holds photographs; these labels describe the intended eventual performance, not verified dance.\n\n"
             f"First final-chorus duet: shot {first_duet['id']}, {first_duet['duration']:.3f} s uninterrupted. Contact and grounded turn remain pending motion review.\n\n"
             "Lin crosses at 160–164 s. Bodies and camera stop from 164 to 179.167 s (first frame at or after 179.13). Yu's answer/crossing finishes by 191.083 s (first frame at or after 191.05). Both remain on I through the final dance and standing sea-facing coda.\n\n"
             "Original portraits remain face authorities; approved compositions and A/B/I masters govern framing, costume and local daylight. Luma remains the scene default; k10 and k42 use documented built-in reframing exceptions after repeated cropped dance masters. Chorus refrains reuse source setups intentionally; no generic skyline filler or synthetic motion is introduced.\n\n"
             "| Shot | In–out timecode | Seconds | Key | Kind | Editorial purpose |\n|---|---|---:|---|---|---|\n")
    table = "".join(f"| {s['id']} | {timecode(s['start_frame'])}–{timecode(s['end_frame'])} | {s['duration']:.3f} | {s['keyframe_id']} | {s['kind']} | {s['purpose']} |\n" for s in timeline)
    (EP/"shotlist.md").write_text(intro+table)
    print(json.dumps({"shots":len(timeline),"keys":len(images),"frames":cursor,"dance_seconds":dance_frames/FPS,
                      "dance_fraction":dance_frames/cursor,"motion_jobs":len(jobs),"motion_seconds":motion['estimated_primary_seconds'],
                      "benchmarks":motion['benchmark_ids'],"first_final_duet_seconds":first_duet['duration']},indent=2))


if __name__ == "__main__":
    main()
