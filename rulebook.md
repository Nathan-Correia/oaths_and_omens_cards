# Oaths & Omens

## Overview

Oaths and Omens is a game of territorial conquest, betrayal, and diplomacy played on a hexagonal map. Players command armies of infantry, cavalry, and archers, and race to be the first to reach 36 victory points by building outposts across the map - and destroying everyone else's. Trading, deceit, and shifting alliances are part of the game — anything goes.

## Pieces

Each player controls one faction and begins the game with a bag containing:

- 12 infantry
- 6 cavalry
- 6 archers
- 4 outposts
- 2 strongholds, 2 storehouses, and 2 temples (outpost upgrades)
- 1 battle die (D6)

The battle die has six faces: **blank**, **shield**, **sword**, **arrow**, **sword + arrow**, and **sword + arrow**.

## Map Creation

The map is built from hexagonal tiles and surrounded by a border frame that marks its edge. Five map sizes are recommended, one for each player count:

| Players | Tiles | Shape |
|---|---|---|
| 4 | 61 | Hexagon, side length 5 |
| 5 | 75 | Truncated triangle: sides alternate between 5 and 6 |
| 6 | 91 | Hexagon, side length 6 |
| 7 | 108 | Truncated triangle: sides alternate between 6 and 7 |
| 8 | 127 | Hexagon, side length 7 |

The method below is our suggested way to generate a map. Players are encouraged to come up with their own maps and build them however they like.

### Suggested map generation

Fill a bag with terrain chits according to the map size:

| Terrain | 61 | 75 | 91 | 108 | 127 |
|---|---|---|---|---|---|
| Lake | 2 | 3 | 3 | 4 | 4 |
| Mountain | 2 | 3 | 3 | 4 | 4 |
| Desert | 4 | 4 | 6 | 6 | 8 |
| Marsh | 4 | 5 | 6 | 7 | 8 |
| Plains | 8 | 10 | 12 | 14 | 16 |

Roughly, this is 10% lake, 10% mountain, 20% desert, 20% marsh, and 40% plains.

Take one plains chit out of the bag and place 3 plains tiles to start the map. Then players take turns drawing a chit from the bag and placing 3 tiles of that terrain. The 3 tiles must be connected to each other and to the map built so far, but may be placed anywhere along its edge and in any shape, with these exceptions:

- **Mountains** must be placed in a line: the third mountain can't be adjacent to both of the first two.
- **Lakes** must be placed in a blob: the third lake must be adjacent to both of the first two.
- **Mountains and lakes** can never be placed touching the border.
- **Mountains and lakes** can never be placed if doing so would cut off part of the map. If a tile would seal off a pocket of the board with no passable route back to the rest of it, place it somewhere else instead. Every non-mountain, non-lake tile must stay reachable by land from every other one.
- **Small holes**: if you place a tile into a hole that is only 1 or 2 spaces big, fill that hole and stop. The rest of that chit's tiles are not placed.

Once the bag is empty, fill any remaining spaces with plains.

## Game Setup

**Placement**: randomize a placement order. Players place their two starting outposts in a snake draft: each player places their first outpost in placement order, then each player places their second outpost in reverse order (so the last player places both of their outposts back to back).

- Your second outpost must be within 3 tiles of your first.
- The normal outpost placement restrictions apply (see Outposts).

Each outpost starts with 3 infantry standing on it. Players start with 0 gold and 0 battle experience.

## Economy

Each turn begins by collecting income, followed by two phases: the **muster phase**, then the **build phase**.

- **Muster phase**: buy infantry and convert infantry into cavalry or archers.
- **Build phase**: build 1 outpost *or* upgrade 1 outpost. Only one of these per turn.
- **Either phase**: draw a god card (at most 1 per turn).

**Income**: every player collects 3 gold per turn, plus 1 gold for each outpost they control. A storehouse adds 1 more gold (see Outpost Upgrades).

**Resources**: each outpost also produces 1 resource per turn, decided by the first rule below that applies to it:

1. **Clay** — the outpost is on a marsh.
2. **Iron** or **fish** — the outpost is next to a mountain (iron) or a lake (fish). If it is next to both, its owner chooses which one to take each turn.
3. **Wood** — the outpost is on plains.

An outpost that matches none of these (a desert not next to a mountain or lake) produces nothing. So a marsh next to a mountain produces clay, but plains next to a mountain produce iron.

**Buying units** (muster phase): infantry cost 2 gold each and are recruited at one of your outposts. Each outpost can recruit at most 1 infantry per turn. Cavalry and archers cannot be purchased with gold — they can only be acquired by spending battle experience (see Battle Experience).

**Production limits**: each player may have at most 12 infantry, 6 cavalry, and 6 archers in play at once. This is a concurrent limit, not a lifetime total — losing a unit immediately frees up capacity to field another of that type.

**Drawing cards** (either phase): you may draw 1 god card per turn for 1 gold (see God Cards).

**Trading**: players may trade gold, resources, cards, and favours with each other. Battle experience, units, and outposts cannot be traded.

## Movement

Units stack together on a tile into a single force called an **army**. An army may hold up to 6 units at a time.

All players move simultaneously: everyone selects and commits their moves for the turn, and all movement is resolved together. If a player does not commit their movement in time, they miss that step.

Movement happens in two parts each turn:

**Regular movement phase**: 3 steps. Each step, every player may move exactly one army 1 hex — even if you control several eligible armies, only one of them may act per step. Any number of units may be split off from that army and moved independently — you don't have to move a whole stack together.

**Cavalry movement phase**: an additional 2 steps, usable only by cavalry units, and subject to the same one-army-per-step rule. Each individual cavalry unit may move up to 2 hexes total during this phase.

If multiple armies end up moving into the same tile, or attack each other, a battle begins. All armies involved in a battle are locked in place — they cannot move again — until the battle phase resolves the fight.

## Battles

There are three ways a battle can begin:

- **Attack/Defense**: an army moves into a tile already occupied by another player's army.
- **Encounter Battle**: two or more armies simultaneously move into the same empty tile.
- **Line Battle**: two armies simultaneously attack each other from adjacent tiles. A line battle takes up both tiles, and an army entering either tile joins the battle as a reinforcement. The winner continues through the opponent: their surviving units end on the tile the losing army held.

Moving into a tile with another player's outpost is always treated as an attack and triggers a battle, even if it has no defending army standing on it — see Outposts for what happens next.

Once triggered, all battle types resolve the same way.

### Reinforcements and overstacking

Because armies lock in place as soon as a battle starts, additional armies are free to move into a battle on a later step of the same movement phase, joining the fight as reinforcements. This means a battle can temporarily exceed the normal 6-unit stack limit while it's ongoing. Once the battle ends, if the winning side has more than 6 units remaining, the winning player must reduce their stack back down to 6 by sending the excess units back to any tile their own units came from during that battle.

Outside of battle, the 6-unit limit is strict: a peaceful move that would merge into a stack and push it past 6 units simply doesn't happen. The move is illegal and the army stays where it started.

### Resolving a Battle

A battle is fought in rounds. In a two-player battle, both players roll their battle die at the same time each round:

| Face | Result |
|------|--------|
| Blank | 0 kills |
| Shield | Cancel 1 kill against you this round |
| Sword | 1 kill |
| Arrow | 1 kill |
| Sword + arrow | 2 kills |

If the rolling player has only 1 unit remaining in the battle, a sword + arrow scores a single kill instead of two.

Both players' kills are applied at the same time — including cases where both armies land kills on each other in the same round.

**Battles with three or more players**: each round, start with a random player and go around the circle. On their turn, a player chooses another player in the battle to attack (or abstains). The attacker and the attacked player both roll and their kills are exchanged as above. Then the next player takes their turn. A player may be attacked more than once in a round.

**Casualties**: when an army takes casualties, its owner chooses which of their units are lost.

A battle continues, round after round, until only one player's army remains standing on the tile. If every remaining player's army is wiped out simultaneously, the tile is left empty with no one victorious.

### Special Unit Abilities

**Archers**: when a player's archers are part of a battle, each archer rolls the battle die once, before the first round of combat begins. Any face with an arrow (arrow or sword + arrow) scores 1 kill against the opposing army with the most units.

**Cavalry**: whenever a cavalry unit dies in battle, its owner immediately rolls the battle die. On a sword + arrow, that cavalry dismounts: a new infantry unit joins the same battle immediately as a live combatant (subject to the normal 12-infantry concurrent limit) — this can even keep an otherwise-defeated army in the fight. On any other face, nothing happens.

## Battle Experience

Whenever a player's unit kills an opposing unit in battle, that player keeps the defeated unit as battle experience. Strongholds also generate battle experience (see Outpost Upgrades).

During the muster phase, a player may spend 2 battle experience to convert one of their own infantry units, anywhere on the board, into a cavalry or archer unit — this is the only way to acquire these unit types.

Battle experience represents accumulated kills and cannot be hoarded indefinitely to deny opponents the ability to spawn units. If a player needs to spawn a unit but all their pieces are currently held by opponents as battle experience, they simply take the piece they need, and a random piece is instead removed from some other player's battle experience holdings to replace it.

## Terrain

| Terrain | Effect | Resource |
|---|---|---|
| **Mountain** | Impassable. | Iron (to adjacent outposts) |
| **Lake** | Impassable. | Fish (to adjacent outposts) |
| **Desert** | Any army that ends its full turn on a desert tile loses 1 unit — unless that tile has an outpost on it, in which case the loss doesn't apply. | — |
| **Marsh** | Any army that enters a marsh tile is frozen and cannot move again for the rest of that turn. | Clay (outpost on it) |
| **Plains** | No special effect. | Wood (outpost on it) |

See Economy for how an outpost's resource is decided.

## Outposts

Outposts are your territory. They earn gold, resources, and victory points, and they can be destroyed.

**Building** (build phase): costs 2 gold and consumes 1 unit (any type) already standing on the tile you're building on. You may build or upgrade only 1 outpost per turn, and you are limited by your outpost pieces (4 per player).

**Placement restrictions**: an outpost cannot be built within 1 tile of any existing outpost — yours or anyone else's.

**Recruiting**: infantry may be purchased at an outpost for 2 gold, at most 1 per outpost per turn.

**Destruction**: entering a tile with an enemy outpost is always treated as an attack and triggers a battle, even if the outpost has no defending army of its own. If, once the battle ends, no other faction's units remain on that tile besides the winner's, the outpost is destroyed — its owner loses it (along with any upgrade on it), and the winner does not take ownership of it, but does keep standing there as normal. The destroyed pieces return to their owner.

**Defense**: an outpost fires 1 free defensive shot the instant its tile is attacked, before the first round of combat — fired even with no defending army present. It rolls the battle die like an archer: any face with an arrow scores 1 kill against the single largest attacking army.

**Respawning**: if a player has no outposts and no units left, they may place 3 infantry on any edge tile of their choosing.

## Outpost Upgrades

During the build phase, instead of building an outpost, you may pay resources to upgrade one of your outposts. Each outpost can hold at most one upgrade, and each player has 2 of each.

| Upgrade | Cost | Effect |
|---|---|---|
| **Stronghold** | 2 wood, 2 fish | +1 battle experience per turn. |
| **Storehouse** | 2 iron, 2 clay | +1 gold per turn. |
| **Temple** | 2 wood, 1 iron, 1 fish, 1 clay | This outpost scores 2 victory points per round instead of 1. |

## God Cards

During the muster or build phase, you may pay 1 gold to draw a god card from the deck, at most once per turn. Keep your cards hidden from other players unless the card says otherwise.

To play a card, pay the resource cost printed on it and follow its text, which also says when it can be played.

## Win Condition

Victory points are the win condition. The first player to reach 36 wins.

At the end of every round, each player earns 1 victory point for each outpost they control (2 for an outpost with a temple). Destroying another player's outpost also immediately awards the winner of that battle 2 victory points.

If, at the end of a round, one or more players are at or above 36 victory points, whoever has the single highest total wins immediately. If the top total is exactly tied between two or more players, whoever of them placed their first outpost later during setup wins the tiebreak.
