# updated for Update 38 - Umbar

import difflib
from typing import Union, Any
import argparse

stables = {
	"ettenmoors": [
		"south bree",
		"thorin's gate",
		"michel delving",
		"rivendell stables"
	],
	"west bree": [
		"adso's camp",
		"buckland",
		"hengstacer farm",
		"south bree",
		"celondim",
		"thorin's gate",
		"ost forod",
		"tinnudir",
		"suri-kyla",
		"esteldin",
		"trestlebridge",
		"hobbiton",
		"michel delving",
		"andrath",
		"herne",
		"mossward"
	],
	"south bree": [
		"minas tirith (after)",
		"osgiliath",
		"west bree",
		"breeland homesteads",
		"combe",
		"galtrev",
		"annak-khurfu",
		"lhanuch",
		"celondim",
		"thorin's gate",
		"stangard",
		"zidir-nesad",
		"magh ashtu",
		"minas tirith",
		"snowbourn",
		"aldburg",
		"helm's deep",
		"forlaw",
		"dale",
		"lake-town",
		"jarnfast",
		"skarhald",
		"ettenmoors",
		"ost guruth",
		"the forsaken inn",
		"michel delving",
		"rivendell stables",
		"hultvis",
		"dol amroth",
		"lond cirion",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"combe": [
		"south bree",
		"celondim",
		"thorin's gate",
		"michel delving",
	],
	"breeland homesteads": [
		"minas tirith (after)",
		"osgiliath",
		"breeland festival grounds",
		"breeland homesteads",
		"south bree",
		"galtrev",
		"annak-khurfu",
		"abodes of erebor",
		"celondim",
		"falathlorn homesteads",
		"thorin's gate",
		"thorin's hall homesteads",
		"zidir-nesad",
		"caras galadhon",
		"estolad lan",
		"magh ashtu",
		"twenty-first hall",
		"snowbourn",
		"aldburg",
		"eastfold hills homesteads",
		"edoras",
		"kingstead meadows homesteads",
		"erebor",
		"felegoth",
		"skarhald",
		"ettenmoors",
		"trestlebridge",
		"michel delving",
		"shire homesteads",
		"the party tree",
		"rivendell stables",
		"cape of belfalas housing neighborhood"
	],
	"the party tree": [],
	"adso's camp": [
		"buckland",
		"west bree"
	],
	"buckland": [
		"west bree",
		"adso's camp",
		"duillond",
		"oatbarton",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"michel delving",
		"needlehole",
		"nobottle",
		"stock",
		"tighfield"
	],
	"tighfield": [
		"nobottle",
		"gamwich",
		"long cleeve",
		"bullroarer's way",
		"foxden road",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"needlehole",
		"brockenborings",
		"stock",
		"buckland"
	],
	"needlehole": [
		"hobbiton",
		"duillond",
		"brockenborings",
		"michel delving",
		"stock",
		"buckland",
		"oatbarton",
		"gamwich",
		"long cleeve",
		"bullroarer's way",
		"nobottle",
		"tighfield",
		"foxden road"
	],
	"foxden road": [
		"nobottle",
		"gamwich",
		"tighfield",
		"long cleeve",
		"bullroarer's way",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"needlehole",
		"brockenborings",
		"stock",
		"buckland"
	],
	"hengstacer farm": [
		"west bree",
		"trestlebridge"
	],
	"thorin's gate": [
		"minas tirith (after)",
		"combe",
		"west bree",
		"annak-khurfu",
		"celondim",
		"duillond",
		"gondamon",
		"noglond",
		"thorin's hall homesteads",
		"ettenmoors",
		"michel delving",
		"mossward"
	],
	"noglond": [
		"gondamon",
		"thorin's gate"
	],
	"gondamon": [
		"duillond",
		"noglond",
		"thorin's gate",
		"thrasi's lodge"
	],
	"thrasi's lodge": [
		"duillond",
		"gondamon",
	],
	"duillond": [
		"buckland",
		"celondim",
		"falathlorn homesteads",
		"gondamon",
		"thorin's gate",
		"thrasi's lodge",
		"oatbarton",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"michel delving",
		"needlehole",
		"nobottle",
		"stock",
		"tighfield"
	],
	"celondim": [
		"combe",
		"west bree",
		"duillond",
		"falathlorn homesteads",
		"thorin's gate",
		"michel delving"
	],
	"michel delving": [
		"minas tirith (after)",
		"buckland",
		"combe",
		"west bree",
		"celondim",
		"duillond",
		"thorin's gate",
		"oatbarton",
		"tinnudir",
		"ettenmoors",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"needlehole",
		"nobottle",
		"shire homesteads",
		"stock",
		"tighfield",
		"mossward",
		"sarn ford"
	],
	"nobottle": [
		"gamwich",
		"tighfield",
		"long cleeve",
		"bullroarer's way",
		"foxden road",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"needlehole",
		"brockenborings",
		"stock",
		"buckland",
	],
	"hobbiton": [
		"buckland",
		"west bree",
		"duillond",
		"oatbarton",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"long cleeve",        
		"michel delving",
		"needlehole",
		"nobottle",
		"shire homesteads",
		"stock",
		"tighfield"
	],
	"long cleeve": [
		"nobottle",
		"gamwich",
		"tighfield",
		"bullroarer's way",
		"foxden road",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"brockenborings",
		"stock",
		"buckland"
	],
	"stock": [
		"buckland",
		"duillond",
		"oatbarton",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"michel delving",
		"needlehole",
		"nobottle",
		"tighfield"
	],
	"brockenborings": [
		"buckland",
		"duillond",
		"oatbarton",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"michel delving",
		"needlehole",
		"nobottle",
		"stock",
		"tighfield"
	],
	"gamwich": [
		"nobottle",
		"tighfield",
		"long cleeve",
		"bullroarer's way",
		"foxden road",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"needlehole",
		"brockenborings",
		"stock",
		"buckland"
	],
	"bullroarer's way": [
		"nobottle",
		"gamwich",
		"tighfield",
		"long cleeve",
		"foxden road",
		"michel delving",
		"duillond",
		"oatbarton",
		"hobbiton",
		"needlehole",
		"brockenborings",
		"stock",
		"buckland"
	],
	"oatbarton": [
		"buckland",
		"duillond",
		"dwaling",
		"high king's crossing",
		"ost forod",
		"tinnudir",
		"brockenborings",
		"bullroarer's way",
		"foxden road",
		"gamwich",
		"hobbiton",
		"long cleeve",
		"michel delving",
		"needlehole",
		"nobottle",
		"stock",
		"tighfield"
	],
	"dwaling": [
		"high king's crossing",
		"oatbarton",
		"ost forod",
		"tinnudir"
	],
	"high king's crossing": [
		"dwaling",
		"oatbarton",
		"ost forod",
		"tinnudir"
	],
	"tinnudir": [
		"west bree",
		"annuminas",
		"dwaling",
		"high king's crossing",
		"oatbarton",
		"ost forod",
		"esteldin",
		"trestlebridge",
		"michel delving"
	],
	"annuminas": [
		"tinnudir"
	],
	"ost forod": [
		"west bree",
		"dwaling",
		"high king's crossing",
		"oatbarton",
		"tinnudir",
		"kauppa-kohta",
		"pynti-peldot",
		"suri-kyla",
		"trestlebridge"
	],
	"amon raith": [
		"esteldin",
		"trestlebridge",
	],
	"trestlebridge": [
		"west bree",
		"hengstacer farm",
		"ost forod",
		"tinnudir",
		"amon raith",
		"esteldin"
	],
	"esteldin": [
		"aughaire",
		"gath forthnir",
		"west bree",
		"tinnudir",
		"amon raith",
		"meluinen",
		"othrikar",
		"trestlebridge",
		"rivendell stables",
		"bail avarc"
	],
	"meluinen": [
		"esteldin",
		"othrikar"
	],
	"othrikar": [
		"esteldin",
		"meluinen"
	],
	"kauppa-kohta": [
		"ost forod",
		"pynti-peldot",
	],
	"pynti-peldot": [
		"ost forod",
		"kauppa-kohta",
		"zigilgund",
		"suri-kyla"
	],
	"suri-kyla": [
		"ost forod",
		"pynti-peldot",
		"zigilgund",
		"kuru-leiri",
		"west bree",
		"gath forthnir",
		"rivendell stables"
	],
	"zigilgund": [
		"pynti-peldot",
		"suri-kyla"
	],
	"kuru-leiri": [
		"suri-kyla"
	],
	"aughaire": [
		"esteldin",
		"gabilshathur",
		"gath forthnir",
		"iorelen's camp"
	],
	"gabilshathur": [
		"gath forthnir",
		"aughaire",
		"iorelen's camp"
	],
	"gath forthnir": [
		"gabilshathur",
		"aughaire",
		"esteldin",
		"rivendell stables",
		"suri-kyla",
		"iorelen's camp",
		"bail avarc"
	],
	"iorelen's camp": [
		"aughaire",
		"gath forthnir",
		"gabilshathur"
	],
	"the forsaken inn": [
		"south bree",
		"ost guruth",
		"breeland homesteads",
		"caranost",
		"scurloc farm",
		"herne"
	],
	"ost guruth": [
		"the forsaken inn",
		"south bree",
		"candaith's encampment",
		"the last bridge",
		"rivendell stables"
	],
	"tornhad": [
		"tham lumren",
		"gaerond",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"scout's camp (high moor)": [
		"tham lumren",
		"gaerond",
		"thorenhad",
		"tornhad",
		"echad candelleth",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"gaerond": [
		"tham lumren",
		"tornhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"the last bridge": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"ost guruth",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"scout's camp (north trollshaws)": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"barachen's camp": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
	],
	"tham lumren": [
		"gaerond",
		"tornhad",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"echad candelleth": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"gwingris",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"thorenhad": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"scout's camp (nan tornaeth)": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (north trollshaws)",
		"the last homely house",
		"rivendell stables",
		"barachen's camp"
	],
	"rivendell stables": [
		"the last homely house",
		"barachen's camp",
		"scout's camp (north trollshaws)",
		"scout's camp (nan tornaeth)",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"tham lumren",
		"gaerond",
		"tornhad",
		"the last bridge",
		"ost guruth",
		"gwingris",
		"gloin's camp",
		"south bree",
		"annak-khurfu",
		"lhanuch",
		"echad dunann",
		"suri-kyla",
		"zidir-nesad",
		"caras galadhon",
		"minas tirith (after)",
		"esteldin",
		"vegbar",
		"ettenmoors",
		"gath forthnir",
		"bail avarc"
	],
	"the last homely house": [
		"tham lumren",
		"gaerond",
		"tornhad",
		"thorenhad",
		"echad candelleth",
		"scout's camp (high moor)",
		"the last bridge",
		"scout's camp (nan tornaeth)",
		"scout's camp (north trollshaws)",
		"rivendell stables",
		"barachen's camp"
	],
	"gloin's camp": [
		"hrimbarg",
		"high crag",
		"vindurhal",
		"rivendell stables"
	],
	"high crag": [
		"vindurhal",
		"gloin's camp",
		"hrimbarg"
	],
	"vindurhal": [
		"high crag",
		"gloin's camp",
		"hrimbarg"
	],
	"hrimbarg": [
		"gloin's camp",
		"vindurhal",
		"high crag",
		"vegbar"
	],
	"gwingris": [
		"echad candelleth",
		"rivendell stables",
		"echad eregion",
		"echad dunann",
		"echad mirobel"
	],
	"echad eregion": [
		"gwingris",
		"echad dunann",
		"echad mirobel"
	],
	"echad dunann": [
		"rivendell stables",
		"echad eregion",
		"echad mirobel",
		"echad dagoras"
	],
	"echad mirobel": [
		"gwingris",
		"echad eregion",
		"echad dunann",
		"echad dagoras"
	],
	"echad dagoras": [
		"maur tulhau",
		"harndirion",
		"echad daervunn",
		"echad mirobel",
		"echad dunann"
	],
	"maur tulhau": [
		"echad dagoras",
		"lhanuch",
		"echad daervunn",
		"harndirion",
		"lintrev"
	],
	"echad daervunn": [
		"echad dagoras",
		"maur tulhau",
		"lhanuch",
		"harndirion",
		"lhan tarren"
	],
	"lhanuch": [
		"echad dagoras",
		"echad daervunn",
		"harndirion",
		"maur tulhau",
		"south bree",
		"inner caras galadhon",
		"galtrev",
		"rivendell stables",
		"lhan garan",
		"lintrev",
		"mossward"
	],
	"harndirion": [
		"echad dagoras",
		"echad daervunn",
		"lhanuch",
		"maur tulhau",
		"echad naeglanc",
	],
	"lhan tarren": [
		"echad naeglanc",
		"galtrev",
		"echad daervunn"
	],
	"echad naeglanc": [
		"lhan tarren",
		"galtrev",
		"harndirion",
	],
	"tal methedras gate": [
		"galtrev"
	],
	"galtrev": [
		"echad naeglanc",
		"lhan tarren",
		"tal methedras gate",
		"rohirrim scout camp",
		"avardin",
		"lhan ros",
		"barnavon",
		"forthbrond",
		"grimbold's camp",
		"dagoras' camp",
		"twenty-first hall",
		"south bree",
		"inner caras galadhon",
		"lhanuch",
		"osgiliath",
		"magh ashtu",
		"dale",
		"jarnfast",
		"skarhald",
		"hultvis",
		"minas tirith (after)",
		"annak-khurfu",
		"zidir-nesad",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)"
	],
	"rohirrim scout camp": [
		"forthbrond",
		"galtrev",
		"barnavon",
	],
	"lhan ros": [
		"avardin",
		"galtrev",
		"barnavon",
	],
	"avardin": [
		"galtrev",
		"lhan ros",
	],
	"barnavon": [
		"lhan ros",
		"galtrev",
		"rohirrim scout camp",
	],
	"wulf's cleft overlook": [
		"barnavon",
	],
	"forthbrond": [
		"rohirrim scout camp",
		"galtrev",
		"grimbold's camp",
	],
	"grimbold's camp": [
		"forthbrond",
		"galtrev",
		"dagoras' camp"
	],
	"dagoras' camp": [
		"grimbold's camp",
		"galtrev",
	],
	"isengard": [
		"aldburg",
		"helm's deep"
	],
	"helm's deep": [
		"grimslade",
		"woodhurst",
		"stoke",
		"edoras",
		"aldburg",
		"twenty-first hall",
		"south bree",
		"isengard"
	],
	"grimslade": [
		"helm's deep"
	],
	"gapholt": [
		"woodhurst",
		"brockbridge"
	],
	"underharrow": [
		"edoras",
		"entwade",
		"middlemead",
		"morlad"
	],
	"edoras": [
		"entwade",
		"middlemead",
		"underharrow",
		"stoke",
		"woodhurst",
		"helm's deep",
		"aldburg",
		"eastfold hills homesteads",
		"kingstead meadows homesteads",
		"minas tirith (after)",
		"zidir-nesad",
		"lond cirion",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)"
	],
	"woodhurst": [
		"gapholt",
		"brockbridge",
		"stoke",
		"helm's deep",
		"edoras",
		"aldburg"
	],
	"brockbridge": [
		"gapholt",
		"woodhurst"
	],
	"middlemead": [
		"entwade",
		"underharrow",
		"edoras"
	],
	"stoke": [
		"oserley",
		"woodhurst",
		"helm's deep",
		"edoras",
		"aldburg"
	],
	"oserley": [
		"stoke"
	],
	"thornhope": [
		"eaworth"
	],
	"dunfast's refugees": [
		"forlaw",
		"byre tor",
		"cerdic's camp",
	],
	"cerdic's camp": [
		"forlaw",
		"dunfast's refugees",
		"byre tor",
	],
	"byre tor": [
		"cerdic's camp",
		"dunfast's refugees",
		"forlaw",
	],
	"scylfig": [
		"harwick",
		"forlaw"
	],
	"forlaw": [
		"scylfig",
		"dunfast's refugees",
		"byre tor",
		"cerdic's camp",
		"south bree",
		"twenty-first hall",
		"harwick",
		"snowbourn"
	],
	"the vile maw": [
		"the rotting cellar"
	],
	"the rotting cellar": [
		"the orc-watch",
		"anazarmekhem",
		"deep descent",
		"the vile maw"
	],
	"anazarmekhem": [
		"the orc-watch",
		"the rotting cellar",
		"twenty-first hall",
		"dolven-view"
	],
	"shadowed refuge": [
		"the orc-watch",
		"twenty-first hall",
		"first hall"
	],
	"the orc-watch": [
		"twenty-first hall",
		"anazarmekhem",
		"shadowed refuge",
		"dolven-view",
		"the rotting cellar"
	],
	"deep descent": [
		"durin's threshold",
		"the rotting cellar",
		"dolven-view"
	],
	"durin's threshold": [
		"dolven-view",
		"deep descent",
		"chamber of the crossroads"
	],
	"dolven-view": [
		"the orc-watch",
		"anazarmekhem",
		"durin's threshold",
		"chamber of the crossroads",
		"deep descent",
		"twenty-first hall",
		"first hall"
	],
	"chamber of the crossroads": [
		"durin's threshold",
		"dolven-view",
		"twenty-first hall",
	],
	"zirakzigil": [
		"jazargund"
	],
	"tharakh bazan": [
		"twenty-first hall",
	],
	"jazargund": [
		"twenty-first hall",
		"zirakzigil",
	],
	"the fanged pit": [
		"twenty-first hall",
	],
	"first hall": [
		"shadowed refuge",
		"twenty-first hall",
		"dolven-view"
	],
	"twenty-first hall": [
		"chamber of the crossroads",
		"jazargund",
		"dolven-view",
		"first hall",
		"the orc-watch",
		"anazarmekhem",
		"shadowed refuge",
		"inner caras galadhon",
		"galtrev",
		"stangard",
		"tharakh bazan",
		"the fanged pit",
		"snowbourn",
		"forlaw",
		"helm's deep",
		"aldburg",
		"dol amroth",
		"minas tirith - main gate",
		"osgiliath",
		"magh ashtu",
		"dale",
		"jarnfast",
		"skarhald",
		"hultvis",
		"annak-khurfu",
		"lond cirion",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)"
	],
	"aldburg": [
		"fenmarch",
		"beaconwatch",
		"edoras",
		"helm's deep",
		"woodhurst",
		"stoke",
		"south bree",
		"isengard",
		"dol amroth",
		"minas tirith",
		"ost rimmon",
		"osgiliath",
		"magh ashtu",
		"dale",
		"jarnfast",
		"skarhald",
		"eastfold hills homesteads",
		"kingstead meadows homesteads"
	],
	"beaconwatch": [
		"fenmarch",
		"aldburg"
	],
	"fenmarch": [
		"aldburg",
		"beaconwatch"
	],
	"walstow": [
		"hytbold",
		"faldham",
		"parth galen",
		"snowbourn"
	],
	"hytbold": [
		"cliving",
		"eaworth",
		"elthengels",
		"faldham",
		"garsfeld",
		"harwick",
		"snowbourn",
		"walstow"
	],
	"garsfeld": [
		"eaworth",
		"hytbold",
		"faldham",
		"snowbourn",
		"walstow"
	],
	"cliving": [
		"eaworth",
		"elthengels",
		"hytbold",
		"faldham",
		"harwick",
		"parth galen",
		"snowbourn"
	],
	"ost rimmon": [
		"war-stead of the rohirrim",
		"minas tirith - main gate",
		"aldburg"
	],
	"faldham": [
		"cliving",
		"elthengels",
		"hytbold",
		"garsfeld",
		"snowbourn",
		"walstow",
	],
	"parth galen": [
		"cliving",
		"eaworth",
		"elthengels",
		"mansig's encampment",
		"floodwend",
		"harwick",
		"snowbourn",
		"walstow"
	],
	"mansig's encampment": [
		"elthengels",
		"parth galen",
		"floodwend",
	],
	"elthengels": [
		"cliving",
		"hytbold",
		"faldham",
		"mansig's encampment",
		"floodwend",
		"harwick",
		"parth galen",
	],
	"floodwend": [
		"elthengels",
		"parth galen",
		"mansig's encampment",
		"harwick",
	],
	"harwick": [
		"cliving",
		"eaworth",
		"elthengels",
		"floodwend",
		"hytbold",
		"stangard",
		"parth galen",
		"snowbourn",
		"scylfig",
		"forlaw"
	],
	"snowbourn": [
		"cliving",
		"eaworth",
		"hytbold",
		"faldham",
		"garsfeld",
		"harwick",
		"parth galen",
		"walstow",
		"stangard",
		"inner caras galadhon",
		"south bree",
		"twenty-first hall",
		"forlaw",
		"entwade",
		"hultvis"
	],
	"eaworth": [
		"cliving",
		"hytbold",
		"garsfeld",
		"harwick",
		"parth galen",
		"snowbourn",
		"thornhope"
	],
	"entwade": [
		"edoras",
		"middlemead",
		"underharrow",
		"snowbourn"
	],
	"brown lands": [
		"rushgore",
		"stangard",
		"thinglad",
		"limlight gorge",
		"parth celebrant",
	],
	"stangard": [
		"thinglad",
		"limlight gorge",
		"parth celebrant",
		"rushgore",
		"brown lands",
		"south bree",
		"twenty-first hall",
		"inner caras galadhon",
		"harwick",
		"snowbourn", 
	],
	"rushgore": [
		"brown lands",
		"parth celebrant",
		"stangard",
		"limlight gorge"
	],
	"parth celebrant": [
		"rushgore",
		"limlight gorge",
		"stangard",
		"thinglad",
		"brown lands"
	],
	"limlight gorge": [
		"brown lands",
		"stangard",
		"parth celebrant",
		"rushgore",
		"thinglad"
	],
	"thinglad": [
		"the vineyards of lorien",
		"stangard",
		"limlight gorge",
		"parth celebrant",
		"brown lands",
		"rushgore"
	],
	"dol amroth": [
		"morlad",
		"calembel",
		"tadrent",
		"south bree",
		"twenty-first hall",
		"aldburg",
		"ethring",
		"linhir",
		"ost anglebed",
		"west pelargir",
		"east pelargir",
		"glaniath",
		"arnach",
		"bar hurin",
		"faramir's lookout",
		"minas tirith",
		"north-gate",
		"osgiliath",
		"magh ashtu",
		"dale",
		"jarnfast",
		"skarhald"
	],
	"morlad": [
		"calembel",
		"tadrent",
		"dol amroth",
		"underharrow",
		"minas tirith"
	],
	"tadrent": [
		"morlad",
		"calembel",
		"dol amroth",
		"minas tirith"
	],
	"calembel": [
		"morlad",
		"tadrent",
		"dol amroth",
		"minas tirith",
		"ethring"
	],
	"ethring": [
		"calembel",
		"linhir",
		"ost anglebed",
		"west pelargir",
		"dol amroth",
		"minas tirith"
	],
	"linhir": [
		"ethring",
		"ost anglebed",
		"west pelargir",
		"dol amroth",
		"minas tirith"
	],
	"ost anglebed": [
		"ethring",
		"linhir",
		"west pelargir",
		"dol amroth",
		"minas tirith"
	],
	"west pelargir": [
		"ethring",
		"linhir",
		"ost anglebed",
		"east pelargir",
		"dol amroth",
		"morlad",
		"minas tirith",
		"calembel",
		"tadrent"
	],
	"east pelargir": [
		"west pelargir",
		"glaniath",
		"arnach",
		"bar hurin",
		"faramir's lookout",
		"minas tirith",
		"north-gate",
		"dol amroth"
	],
	"glaniath": [
		"east pelargir",
		"arnach",
		"bar hurin",
		"faramir's lookout",
		"minas tirith",
		"dol amroth"
	],
	"arnach": [
		"east pelargir",
		"glaniath",
		"bar hurin",
		"faramir's lookout",
		"minas tirith",
		"dol amroth"
	],
	"bar hurin": [
		"east pelargir",
		"glaniath",
		"arnach",
		"faramir's lookout",
		"minas tirith",
		"dol amroth"
	],
	"war-stead of the rohirrim": [
		"ost rimmon",
		"minas tirith - main gate"
	],
	"minas tirith": [
		"north-gate",
		"crithost",
		"morlad",
		"calembel",
		"tadrent",
		"dol amroth",
		"ethring",
		"linhir",
		"ost anglebed",
		"west pelargir",
		"east pelargir",
		"glaniath",
		"arnach",
		"bar hurin",
		"faramir's lookout",
		"south bree",
		"twenty-first hall",
		"aldburg",
		"minas tirith - soldiers' tier",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - masters' tier",
		"ost rimmon",
		"war-stead of the rohirrim",
		"osgiliath",
		"magh ashtu",
		"dale",
		"minas tirith (after)"
	],
	"minas tirith - main gate": [
		"north-gate",
		"crithost",
		"morlad",
		"calembel",
		"tadrent",
		"dol amroth",
		"ethring",
		"linhir",
		"ost anglebed",
		"west pelargir",
		"east pelargir",
		"glaniath",
		"arnach",
		"bar hurin",
		"faramir's lookout",
		"south bree",
		"twenty-first hall",
		"aldburg",
		"minas tirith - soldiers' tier",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - masters' tier",
		"ost rimmon",
		"war-stead of the rohirrim",
		"osgiliath",
		"magh ashtu",
		"dale",
		"minas tirith (midsummer)"
	],
	"minas tirith - soldiers' tier": [
		"minas tirith - main gate",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - masters' tier",
	],
	"minas tirith - masters' tier": [
		"minas tirith - main gate",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - soldiers' tier",
	],
	"minas tirith (after)": [
		"aragorn's pavilion",
		"osgiliath",
		"henneth annun",
		"camp of the host",
		"minas tirith (midsummer)",
		"zidir-nesad"
	],
	"minas tirith - sages' tier": [
		"minas tirith - main gate",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - soldiers' tier",
		"minas tirith - masters' tier"
	],
	"minas tirith - craftsmen's tier": [
		"minas tirith - main gate",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - soldiers' tier",
		"minas tirith - masters' tier"
	],
	"north-gate": [
		"minas tirith - main gate",
		"crithost",
		"dol amroth",
		"east pelargir"
	],
	"minas tirith (midsummer)": [
		"beorninghus",
		"south bree",
		"caras galadhon",
		"edoras",
		"erebor",
		"felegoth",
		"galtrev",
		"minas tirith",
		"osgiliath",
		"skarhald",
		"thorin's gate",
		"minas tirith - craftsmen's tier",
		"minas tirith - players' tier",
		"minas tirith - sages' tier",
		"minas tirith - soldiers' tier",
		"annak-khurfu",
		"zidir-nesad",
		"rivendell stables"
	],
	"minas tirith - players' tier": [
		"minas tirith - main gate",
		"minas tirith - craftsmen's tier",
		"minas tirith - sages' tier",
		"minas tirith - soldiers' tier",
		"minas tirith - masters' tier"
	],
	"aragorn's pavilion": [
		"minas tirith",
		"osgiliath",
		"henneth annun",
		"camp of the host"
	],
	"crithost": [
		"minas tirith - main gate",
		"north-gate"
	],
	"osgiliath": [
		"minas tirith",
		"aragorn's pavilion",
		"henneth annun",
		"camp of the host",
		"south bree",
		"twenty-first hall",
		"aldburg",
		"galtrev",
		"minas tirith - main gate",
		"hultvis",
		"estolad lan",
		"minas tirith (midsummer)",
		"annak-khurfu"
	],
	"faramir's lookout": [
		"minas tirith - main gate",
		"bar hurin",
		"east pelargir",
		"glaniath",
		"arnach",
		"dol amroth"
	],
	"estolad lan": [
		"echad taerdim",
		"echad uial",
		"minas morgul",
		"magh ashtu",
		"henneth annun",
		"osgiliath",
		"taen orwath",
		"hultvis"
	],
	"minas morgul": [
		"echad taerdim",
		"echad uial",
		"taen orwath",
		"estolad lan"
	],
	"echad taerdim": [
		"echad uial",
		"minas morgul",
		"taen orwath",
		"estolad lan"
	],
	"taen orwath": [
		"echad taerdim",
		"echad uial",
		"minas morgul",
		"estolad lan"
	],
	"echad uial": [
		"echad taerdim",
		"minas morgul",
		"magh ashtu",
		"taen orwath",
		"estolad lan"
	],
	"magh ashtu": [
		"udun foothold",
		"ruins of dingarth",
		"agarnaith ranger's camp",
		"ruins of dingarth",
		"south bree",
		"twenty-first hall",
		"galtrev",
		"aldburg",
		"dol amroth",
		"minas tirith - main gate",
		"hultvis",
		"echad uial",
		"estolad lan"
	],
	"agarnaith ranger's camp": [
		"udun foothold",
		"ruins of dingarth",
		"magh ashtu"
	],
	"adambel": [
		"dingarth",
		"echad-in-edhil",
		"barthost"
	],
	"barthost": [
		"dingarth",
		"adambel",
		"echad-in-edhil"
	],
	"ruins of dingarth": [
		"udun foothold",
		"agarnaith ranger's camp",
		"magh ashtu",
	],
	"dingarth": [
		"adambel",
		"barthost",
		"echad-in-edhil"
	],
	"echad-in-edhil": [
		"dingarth",
		"adambel",
		"barthost"
	],
	"udun foothold": [
		"the slag-hills",
		"ruins of dingarth",
		"magh ashtu",
		"agarnaith ranger's camp",
	],
	"the slag-hills": [
		"udun foothold",
		"camp of the host",
		"osgiliath"
	],
	"camp of the host": [
		"minas tirith",
		"aragorn's pavilion",
		"henneth annun",
		"osgiliath",
		"the slag-hills"
	],
	"henneth annun": [
		"minas tirith",
		"aragorn's pavilion",
		"camp of the host",
		"osgiliath",
		"estolad lan"
	],
	"ost galadh": [
		"echad sirion",
		"the haunted inn",
		"estolad mernael",
		"thangulhad",
		"mithechad",
		"helethir",
		"inner caras galadhon",
		"tham taerdol"
	],
	"caras galadhon": [
		"mekhem-bizru",
		"echad andestel",
		"the vineyards of lorien",
		"cerin amroth",
		"arhaim",
		"minas tirith (midsummer)",
		"annak-khurfu",
		"zidir-nesad",
		"rivendell stables"
	],
	"the vineyards of lorien": [
		"mekhem-bizru",
		"echad andestel",
		"caras galadhon",
		"cerin amroth",
		"thinglad"
	],
	"mithechad": [
		"echad sirion",
		"the haunted inn",
		"ost galadh",
		"estolad mernael",
		"thangulhad",
		"helethir"
	],
	"helethir": [
		"echad sirion",
		"the haunted inn",
		"ost galadh",
		"estolad mernael",
		"thangulhad",
		"mithechad"
	],
	"thangulhad": [
		"echad sirion",
		"the haunted inn",
		"ost galadh",
		"estolad mernael",
		"mithechad",
		"helethir",
		"tham taerdol"
	],
	"estolad mernael": [
		"echad sirion",
		"the haunted inn",
		"ost galadh",
		"mithechad",
		"helethir",
		"thangulhad"
	],
	"the haunted inn": [
		"echad sirion",
		"ost galadh",
		"estolad mernael",
		"mithechad",
		"helethir",
		"thangulhad",
	],
	"echad sirion": [
		"the haunted inn",
		"ost galadh",
		"estolad mernael",
		"mithechad",
		"helethir",
		"thangulhad"
	],
	"inner caras galadhon": [
		"twenty-first hall",
		"galtrev",
		"rivendell stables",
		"ost galadh",
		"lhanuch",
		"stangard",
		"snowbourn"
	],
	"cerin amroth": [
		"mekhem-bizru",
		"the vineyards of lorien",
		"caras galadhon",
		"echad andestel",
	],
	"echad andestel": [
		"mekhem-bizru",
		"the vineyards of lorien",
		"caras galadhon",
		"cerin amroth",
	],
	"mekhem-bizru": [
		"the vineyards of lorien",
		"caras galadhon",
		"echad andestel",
		"cerin amroth"
	],
	"arhaim": [
		"blomgard",
		"beorninghus",
		"hultvis",
		"vegbar",
		"caras galadhon"
	],
	"gladdenmere - southern shore": [
		"gladdenmere - northern shore",
	],
	"gladdenmere - northern shore": [
		"gladdenmere - southern shore",
	],
	"blomgard": [
		"beorninghus",
		"hultvis",
		"vegbar",
		"arhaim",
	],
	"hultvis": [
		"beorninghus",
		"blomgard",
		"vegbar",
		"arhaim",
		"south bree",
		"erebor",
		"galtrev",
		"magh ashtu",
		"osgiliath",
		"skarhald",
		"snowbourn",
		"twenty-first hall",
		"estolad lan"
	],
	"vegbar": [
		"blomgard",
		"arhaim",
		"hultvis",
		"beorninghus",
		"hrimbarg",
		"rivendell stables"
	],
	"beorninghus": [
		"blomgard",
		"vegbar",
		"hultvis",
		"arhaim",
		"felegoth",
		"south bree",
		"limlok",
		"minas tirith (midsummer)"
	],
	"tham taerdol": [
		"felegoth",
		"lake-town",
		"dale",
		"erebor",
		"ost galadh",
		"thangulhad"
	],
	"limlok": [
		"thokvist",
		"hlithseld",
		"lyndelby",
		"beorninghus"
	],
	"felegoth": [
		"tham taerdol",
		"lake-town",
		"dale",
		"erebor",
		"beorninghus",
		"minas tirith (midsummer)",
		"annak-khurfu",
		"zidir-nesad",
		"lond cirion",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)"
	],
	"lake-town": [
		"tham taerdol",
		"felegoth",
		"dale",
		"erebor",
		"south bree"
	],
	"dale": [
		"tham taerdol",
		"felegoth",
		"lake-town",
		"erebor",
		"south bree",
		"twenty-first hall",
		"galtrev",
		"aldburg",
		"dol amroth",
		"minas tirith - main gate",
		"skald's drop",
		"hammerstead",
		"jarnfast",
		"dom goru",
		"skarhald"
	],
	"erebor": [
		"dale",
		"tham taerdol",
		"felegoth",
		"lake-town",
		"skald's drop",
		"hammerstead",
		"jarnfast",
		"dom goru",
		"skarhald",
		"hultvis",
		"minas tirith (midsummer)",
		"annak-khurfu",
		"zidir-nesad",
		"lond cirion",
		"linhir (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"skald's drop": [
		"dale",
		"erebor",
		"hammerstead",
		"jarnfast",
		"dom goru",
		"skarhald"
	],
	"hammerstead": [
		"dale",
		"erebor",
		"skald's drop",
		"jarnfast",
		"dom goru",
		"skarhald"
	],
	"jarnfast": [
		"dale",
		"erebor",
		"skald's drop",
		"hammerstead",
		"dom goru",
		"skarhald",
		"south bree",
		"twenty-first hall",
		"galtrev",
		"aldburg",
		"dol amroth",
		"minas tirith - main gate"
	],
	"dom goru": [
		"dale",
		"erebor",
		"skald's drop",
		"hammerstead",
		"jarnfast",
		"skarhald",
	],
	"skarhald": [
		"dale",
		"erebor",
		"skald's drop",
		"hammerstead",
		"jarnfast",
		"dom goru",
		"hultvis",
		"south bree",
		"twenty-first hall",
		"galtrev",
		"aldburg",
		"dol amroth",
		"minas tirith - main gate",
		"hlithseld",
		"minas tirith (midsummer)",
		"annak-khurfu",
		"zidir-nesad"
	],
	"annak-khurfu": [
		"zudramdan",
		"galtrev",
		"skarhald",
		"thorin's gate",
		"minas tirith (midsummer)",
		"osgiliath",
		"caras galadhon",
		"hlithseld",
		"twenty-first hall",
		"drenghol",
		"erebor",
		"felegoth",
		"rivendell stables",
		"the war of three peaks"
	],
	"the war of three peaks": [],
	"breeland festival grounds": [],
	"candaith's encampment": [],
	"hlithseld": [
		"limlok",
		"thokvist",
		"lyndelby",
		"skarhald",
		"annak-khurfu"
	],
	"thokvist": [
		"limlok",
		"hlithseld",
		"lyndelby"
	],
	"lyndelby": [
		"limlok",
		"thokvist",
		"hlithseld",
	],
	"zudramdan": [
		"annak-khurfu",
		"drenghol",
		"leitstath"
	],
	"drenghol": [
		"zudramdan",
		"annak-khurfu",
		"maergrind"
	],
	"maergrind": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"drenghol",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"imrekh-guthlu": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"aslif": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"watcher's roost": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"zidir-nesad": [
		"grumachath",
		"leitstath",
		"caras galadhon",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"edoras",
		"erebor",
		"felegoth",
		"galtrev",
		"watcher's roost",
		"asbaj-khirfin",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru",
		"minas tirith (midsummer)",
		"minas tirith",
		"skarhald",
		"south bree",
		"rivendell stables"
	],
	"hagbuth": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"bazanmanar": [
		"grumachath",
		"leitstath",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"fellgat": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"ibdekh-buzru"
	],
	"ibdekh-buzru": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat"
	],
	"asbaj-khirfin": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"bargstad": [
		"grumachath",
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"fellgat",
		"ibdekh-buzru"
	],
	"leitstath": [
		"grumachath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru",
		"zudramdan"
	],
	"grumachath": [
		"leitstath",
		"bazanmanar",
		"hagbuth",
		"aslif",
		"watcher's roost",
		"asbaj-khirfin",
		"zidir-nesad",
		"maergrind",
		"imrekh-guthlu",
		"bargstad",
		"fellgat",
		"ibdekh-buzru"
	],
	"eastfold hills homesteads": [
		"aldburg",
		"edoras"
	],
	"kingstead meadows homesteads": [
		"edoras",
		"aldburg" 
	],
	"sarn ford": [
		"andrath",
		"caranost",
		"scurloc farm",
		"herne",
		"michel delving",
		"tharbad"
	],
	"andrath": [
		"west bree",
		"caranost",
		"scurloc farm",
		"herne",
		"sarn ford",
		"tharbad"
	],
	"herne": [
		"andrath",
		"west bree",
		"caranost",
		"scurloc farm",
		"the forsaken inn",
		"lhan garan",
		"mossward",
		"rivendell stables",
		"sarn ford",
		"tharbad"
	],
	"caranost": [
		"andrath",
		"scurloc farm",
		"the forsaken inn",
		"herne",
		"sarn ford",
		"tharbad"
	],
	"tharbad": [
		"andrath",
		"caranost",
		"scurloc farm",
		"herne",
		"lhan garan",
		"mossward",
		"sarn ford"
	],
	"mossward": [
		"west bree",
		"caras gelebren",
		"celondim",
		"clegur",
		"glyn helyg",
		"herne",
		"lhan garan",
		"lhanuch",
		"lintrev",
		"michel delving",
		"rivendell stables",
		"tharbad",
		"thorin's gate",
		"western eregion"
	],
	"clegur": [
		"caras gelebren",
		"glyn helyg",
		"lhan garan",
		"lintrev",
		"mossward",
		"western eregion"
	],
	"glyn helyg": [
		"caras gelebren",
		"clegur",
		"lhan garan",
		"lintrev",
		"mossward",
		"western eregion"
	],
	"lintrev": [
		"caras gelebren",
		"clegur",
		"glyn helyg",
		"lhan garan",
		"lhanuch",
		"maur tulhau",
		"mossward",
		"western eregion"
	],
	"caras gelebren": [
		"clegur",
		"echad mirobel",
		"glyn helyg",
		"lhan garan",
		"lintrev",
		"mossward",
		"western eregion"
	],
	"lhan garan": [
		"caras gelebren",
		"clegur",
		"glyn helyg",
		"herne",
		"lhanuch",
		"lintrev",
		"mossward",
		"tharbad",
		"western eregion"
	],
	"scurloc farm": [
		"andrath",
		"caranost",
		"the forsaken inn",
		"herne",
		"sarn ford",
		"tharbad"
	],
	"western eregion": [
		"caras gelebren",
		"clegur",
		"echad mirobel",
		"glyn helyg",
		"lhan garan",
		"lintrev",
		"mossward"
	],
	"bail avarc": [
		"esteldin",
		"rivendell stables",
		"gath forthnir"
	],
	"umbar baharbel - west gate": [
		"jax phanal",
		"khutra",
		"rakhatab",
		"umbar baharbel - east gate",
		"umbar baharbel - north gate"
	],
	"umbar baharbel - east gate": [
		"umbar baharbel - north gate"
	],
	"umbar baharbel - north gate": [
		"umbar baharbel - east gate",
		"umbar baharbel - west gate"
	],
	"khutra": [
		"jax phanal",
		"rakhatab",
		"umbar baharbel - west gate"
	],
	"rakhatab": [
		"jax phanal",
		"khutra",
		"umbar baharbel - west gate"
	],
	"jax phanal": [
		"khutra",
		"rakhatab",
		"umbar baharbel - west gate",
		"bel inzul",
		"halrax"
	],
	"bel inzul": [
		"kafagar",
		"voyage's end",
		"mar naphra",
		"halrax",
		"jax phanal"
	],
	"halrax": [
		"kafagar",
		"voyage's end",
		"mar naphra",
		"jax phanal",
		"bel inzul",
		"umbar baharbel - west gate",
		"lond cirion",
		"dol amroth (king's gondor)",
		"pelargir west gate (king's gondor)" # boat
	],
	"mar naphra": [
		"kafagar",
		"voyage's end",
		"halrax",
		"bel inzul"
	],
	"voyage's end": [
		"kafagar",
		"mar naphra",
		"halrax",
		"bel inzul"
	],
	"kafagar": [
		"voyage's end",
		"mar naphra",
		"halrax",
		"bel inzul"
	],
	"dol amroth (king's gondor)": [  # NEEDS CHECKING AT LOCATION
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"lancrath",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"linhir (king's gondor)",
		"pelargir west gate (king's gondor)",
		"minas tirith (after)",
		"rivendell stables",
		"south bree",
		"galtrev",
		"twenty-first hall",
		"erebor",
		"felegoth",
		"edoras",
		"lond cirion",
		"melgobas"
	],
	"ost lontir": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"tadrent (king's gondor)": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"dol amroth (king's gondor)"
	],
	"sardol": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"morlad (king's gondor)": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"lancrath": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"dinadab": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"lothgobel",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"lothgobel": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"calembel (king's gondor)",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"calembel (king's gondor)": [
		"parth rest",
		"barad rill",
		"ethring (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"ethring (king's gondor)": [
		"parth rest",
		"barad rill",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"parth rest": [
		"ethring (king's gondor)",
		"barad rill",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)",
		"linhir (king's gondor)"
	],
	"barad rill": [
		"ethring (king's gondor)",
		"parth rest",
		"calembel (king's gondor)",
		"lothgobel",
		"dinadab",
		"lancrath",
		"morlad (king's gondor)",
		"sardol",
		"ost lontir",
		"tadrent (king's gondor)",
		"dol amroth (king's gondor)"
	],
	"linhir (king's gondor)": [
		"twenty-first hall",
		"aerthir",
		"arnach (king's gondor)",
		"south bree",
		"furukzahar",
		"zarsatrad",
		"edoras",
		"erebor",
		"erynos",
		"felegoth",
		"galtrev",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"malbarth",
		"minas tirith (after)",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"rivendell stables",
		"tumladen",
		"dol amroth (king's gondor)",
		"parth rest"
	],
	"malbarth": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
		"linhir (king's gondor)"
	],
	"aerthir": [
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
	],
	"ost anglebed (king's gondor)": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
	],
	"furukzahar": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
	],
	"zarsatrad": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
	],
	"erynos": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
		"tumladen",
	],
	"pelargir west gate (king's gondor)": [
        "lond cirion",
		"minas tirith (after)",
		"south bree",
		"galtrev",
		"aerthir",
		"arnach (king's gondor)",
		"erynos",
		"furukzahar",
		"glaniath (king's gondor)",
		"halach",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed",
		"pelargir east gate (king's gondor)",
		"the harlond",
		"tumladen",
		"zarsatrad",
		"twenty-first hall",
		"edoras",
		"erebor",
		"felegoth",
		"rivendell stables",
		# "dol amroth (king's gondor)", # boat
		# "halrax", # boat
		# "umbar baharbel", # boat
	],
	"pelargir east gate (king's gondor)": [
		"twenty-first hall",
		"aerthir",
		"arnach (king's gondor)",
		"south bree",
		"furukzahar",
		"zarsatrad",
		"edoras",
		"erebor",
		"erynos",
		"felegoth",
		"galtrev",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"minas tirith (after)",
		"ost anglebed (king's gondor)",
		"pelargir west gate (king's gondor)",
		"rivendell stables",
		"tumladen",
	],
	"tumladen": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"glaniath (king's gondor)",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"glaniath (king's gondor)": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"tumladen",
		"halach",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"halach": [
		"aerthir",
		"arnach (king's gondor)",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"tumladen",
		"glaniath (king's gondor)",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"arnach (king's gondor)": [
		"aerthir",
		"halach",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"tumladen",
		"glaniath (king's gondor)",
		"the harlond",
		"imloth melui",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"imloth melui": [
		"aerthir",
		"halach",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"tumladen",
		"glaniath (king's gondor)",
		"the harlond",
		"arnach (king's gondor)",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"the harlond": [
		"aerthir",
		"halach",
		"furukzahar",
		"zarsatrad",
		"erynos",
		"tumladen",
		"glaniath (king's gondor)",
		"imloth melui",
		"arnach (king's gondor)",
		"linhir (king's gondor)",
		"malbarth",
		"ost anglebed (king's gondor)",
		"pelargir east gate (king's gondor)",
		"pelargir west gate (king's gondor)",
	],
	"iaphel": [
		"melgobas",
		"barad faen",
		"lond cirion",
		"ost arndir",
		"mereham"
	],
	"lond cirion": [
		"melgobas",
		"barad faen",
		"iaphel",
		"ost arndir",
		"mereham",
		"dol amroth (king's gondor)",
		"pelargir west gate (king's gondor)",
		"minas tirith (after)",
		"rivendell stables",
		"south bree",
		"galtrev",
		"twenty-first hall",
		"erebor",
		"felegoth",
		"edoras"
	],
	"ost arndir": [
		"melgobas",
		"barad faen",
		"lond cirion",
		"iaphel",
		"mereham"
	],
	"barad faen": [
		"melgobas",
		"lond cirion",
		"iaphel",
		"ost arndir",
		"mereham"
	],
	"mereham": [
		"melgobas",
		"barad faen",
		"lond cirion",
		"iaphel",
		"ost arndir"
	],
	"melgobas": [
		"barad faen",
		"lond cirion",
		"iaphel",
		"ost arndir",
		"mereham",
		"dol amroth (king's gondor)"
	],
	"shire homesteads": [],
	"thorin's hall homesteads": [],
	"abodes of erebor": [],
	"cape of belfalas housing neighborhood": [],
	"falathlorn homesteads": [],
}


def ask(question: str="", 
	default: str="", 
	_type: Union[int, str, float]=str, 
	force_type: bool=True, 
	list_type: Union[int, str, float]=str, 
	require_answer: bool=False,
	pre_cursor: str="",
	post_cursor: str="\n> ",
	enforce_rule=lambda x: x
	) -> Any:
	""" Seeks input(question) from the user.
	
	:Parameters:
	question (type: str) -> Output to the user
	default (type: str, "y" or "n") -> If set, determines the default behaviour for the 
		enter key. Requires the user to input a "y", "n" in their answer or enter key only.
		If set, user input returns boolean True or False. Ignores _type and force_type.
	_type (type: class int, class str, or class float) -> Which data type the user's 
		response should be.
	force_type (type: boolean) -> Whether the user's input will be returned as the _type 
		specified rather than Python's default (string).
	list_type (type: class int, class str, or class float) -> What data type all comma 
		separated user inputs should be. Ignores force_type.
	require_answer (type: boolean) -> Whether to allow empty input from the user.
	pre_cursor (type: str) -> str to display before question
	post_cursor (type: str) -> str to display after question
	
	:Returns:
	The user's input, which must match the format of _type parameter, and will be returned as 
	the type specified by the force_type parameter
	"""
	
	for param in [question, pre_cursor, post_cursor]:
		assert isinstance(param, str), f"question, pre_cursor, and post_cursor parameters should be strings"
	assert default.lower() in ["y", "n", ""], "'default' parameter should be 'y', 'n' or empty string"
	assert _type in [str, int, float, list], "'_type' parameter should be either str, int, float, or list"
	
	def validate_type(_input, _type, default):
		""" Internal function used only by ask() """
		def rule_enforcer(x):
			""" Internal function used only by validate_type """
			if enforce_rule(x):
				return x
			else:
				raise ValueError("Input does not meet requirements.")
		
		if default:
			values = {
				"y": {"value": True, "opposite": "n"}, 
				"n": {"value": False, "opposite": "y"}
			}
			values[""] = values[default]
			if _input.strip() == "":
				return values[""]["value"]
			if default in _input: 
				return values[default]["value"]
			if values[default]["opposite"] in _input: 
				return not values[default]["value"]
			raise ValueError(f"Please input y, n, or press enter (assumes '{default}').")
		
		if not require_answer and not _input and not _type == list:
			return ""
			
		if _type == str:
			if require_answer and _input == "":
				raise ValueError("Please input some text.")
			else:
				return rule_enforcer(_input)
		elif _type == int:
			if _input.lstrip("-").isdigit():
				if force_type:
					return rule_enforcer(int(_input))
				else:
					return rule_enforcer(_input)
			else:
				raise ValueError("Please input a whole number.")
		elif _type == float:
			try:
				float(_input)
				if force_type:
					return rule_enforcer(float(_input))
				else:
					return rule_enforcer(str(float(_input)))
			except:
				raise ValueError("Please input a number.")
		elif _type == list:
			if not _input.strip():
				return rule_enforcer([])
			list_answers = []
			for csv in _input.split(","):
				if csv.strip():
					list_answers.append(validate_type(csv.strip(), list_type, default=""))
			return rule_enforcer(list_answers)
		
	if default:
		default = default.lower()
		question = f"{question} {'Y/n' if default == 'y' else 'y/N'}"
		
	answer = None
	while answer is None:
		user_input = input(f"{pre_cursor}{question}{post_cursor}")
		try:
			answer = validate_type(user_input, _type, default)
		except ValueError as err:
			print(err)
	return answer


def find_all_paths(stables, start, end, path=[]):
	path = path + [start]
	if len(path) > 6: return
	if start == end:
		return [path]
	if start not in stables:
		print(f"ERROR: '{start}' listed as a stable destination, but isn't in the list of stables.")
		return []
	paths = []
	for node in stables[start]:
		if node not in path:
			newpaths = find_all_paths(stables, node, end, path)
			if newpaths:
				for newpath in newpaths:
					paths.append(newpath)
	return paths


def who_can_travel_to(place):
	""" function not currently used"""
	if place not in stables:
		return [f"No such stable '{place}'."]
	return [stable for stable in stables if place in stables[stable]]
	

def suggest_stable(place):
	suggested_stables = set()
	for word in place.split():
		for stable in stables:
			if word in stable.split():
				suggested_stables.add(stable)
	return suggested_stables


def print_suggested(_type, queried_stable):
	suggested_stables = suggest_stable(queried_stable)
	if not suggested_stables:
		suggested_stables = difflib.get_close_matches(queried_stable, stables.keys())
		if not suggested_stables:
			suggested_stables = ["None found that match your query."]
	new_line = "\n"
	print(f"\nCould not find the {_type} stable '{queried_stable}'. Perhaps you mean:\n - {f'{new_line} - '.join(suggested_stables)}")


def get_number_of_results(num):
	if num:
		return int(num)
	elif args.source and args.destination and not num:
		return 5
	else:
		results = ask("Number of results:", _type=int, enforce_rule=lambda x: x>0, post_cursor=" ")
	if results == "": 
		results = 5
	return results


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Provide a source, destination, and desired number of results (number)")
	parser.add_argument("source", nargs="?", help="Stable to leave from")
	parser.add_argument("destination", nargs="?", help="Stable to arrive at")
	parser.add_argument("number", type=int, nargs="?", help="Number of results to return")
	args = parser.parse_args()
	
	while True:
		source = (args.source or ask("\nFrom:", require_answer=True, post_cursor=" ")).lower()
		destination = (args.destination or ask("To:", require_answer=True, post_cursor=" ")).lower()
		results = get_number_of_results(args.number)

		quit = False
		for _type, _input in (("source", source), ("destination", destination)):
			if _input not in stables:
				print_suggested(_type, _input)
				quit = True
		if quit:
			continue

		paths = find_all_paths(stables, source, destination)
		if paths:
			print(f"\n{len(paths):,} paths found:\n")
			for i, path in enumerate(sorted(paths, key=len)[:results], 1):
				print(f"{i:>{len(str(results))}})  ({len(path)} hops)", " -> ".join(path))
		else:
			print("No paths found.")

		if any([args.source, args.destination, args.number]):
			break