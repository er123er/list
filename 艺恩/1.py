import json
import pprint
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests

with open('1.js', 'r', encoding='utf-8') as f:
    js = f.read()

# data = 'C4CCEB34D189C39497A818594C1CEC79C6B4FB3D2F2FA5FC20C646ED0EF4FB89EB5713090380CC622E51C2FFFEC19699E29F8A72918297D1F102EBC104E858D957D5D191359E2937BC62FDC44AF1360E3B1017BB89F884A8F860450F53BC64CDF36A798FF0BF75996E0E955FD4FCAC56F16F01305E7AEEF70C4C09838F164FFE151F1D7B2FDB10C305D13525F359B82BAB1E5334B7B798AD15822ABC659219B773117016A6FDF75BB1F87E1C6C90649B3B7C6D4886E63F84BD5C3B02800DA9C5093F88B8E3D80EF7B28B941A116FBFEC8A8D604A9E906A0B08D0060D58AA032C138799082B8B90F825BE43C3136576E08960AD236F80322311D677A81774C03898ECBE658AE88C413BED6C8CCE8ECA0B833942CBB663999B9A9AB11E7F1072F6E566216B4DD06B5C752D1886CBDF74CD552AD1FA8221FD8B39C3D96385CD6E3E191FBC2BF673963F7A6B89C76EFEDBAF405F1DE25FACE8291B5B71653EA8FAC59DF57F91DA34E5A3B90BFE79E3EFA3AF42E2E7D0E63F6971EBB71CC67166457454A52EBB060E904720173430D7AAF783FBDD5D63ECC26E255E4456B3D0EB9B4BD8CBE5416BBAE6B5168515578518DFC724700DE90C7814FFC34E6310368866251CEC9104A3B18E99F03AC465D166044CC3A7D49477302EC150C05B1D442BF1A28FA12E5CA70DE9C9B1B8643075FBB97B94D1DA83B3B93D03BAA81B25E41371F3A8E8C846B4EB28C6F33E06AF92C74A3B04E118806E3C25DD14E54CED691601A4DCA9A73FAD5572AF8A0C11A03948E4DEF672E8CCD622A34F363261EC772BE159E598A2C8AEC2A51503D1292AACA31F5B1D5E15BF5EC49995B080093CAA5EA72F04592BC97BE37E4E287583C7C8E3DCAFA2DF9E0942E4B3AA14F1CD6EBEBD64509DF53536874C12A66FDD16C854F7017CBECEA9B219F455DD412EA9D12CB2DB30ED338379FD1242B45353F1E24ABB0BBEDE3EE631C189E16E7D9BF44FFF390EE556B4F9EAFA970AE4485387A0592E2D09731E9E5B870CDD229C9FC4A270736B4C95007D08E37D910E242E2D8D057F33947EB611EBCFC390E21DD58A87A0C5F1AC41A9CCAC23C956943DB8870F2EEEE686D36353EC924BEED6F41D791EC6163117B482B5E5DEA65DB1B83E4656E072296134F4A7261BF2975F58BCA31584D65AD73B8CFF536EC19699E29F8A729576B9BABA4ED74464E858D957D5D1913D7BFAA8677435661F8EC1AFF664F1CD1E4D91011602A56EC1E6BA40AA5864B04F0ED4485656EB3C509D95FA52A6BD546E54CEFF043B5730CEAC0E2009A0BDE989648DDE50A37BBEAA6588613296841EEBD2DA4433060ECE29B02850CCBE67AC6B3D21F233744B1478FAEB3B93E89801254A60A80AC2906931D07F4526A48A2BCCFE0236306F0DFCBF02AB8C1EC04F3DC42712B5CF43F06640417825079B49F6913341EB3E5CE8002B384945FE66450C7403B712FC7EBA2C6E67E643CD9776CB66411C3C0E856A6ADC9E8FEA8736B38B5DCD4A92B8F354D2CFAD038DC12637BC44D33EA993BD9826D09DBA935A3D4A7DF570133449E826F73D2B80AB5F8FEC2A3985C0CB0F7476A2F243F5946A1C8086BBEB16B48EC0E957A3EFA3AF42E2E7D0E63F6971EBB71CC672ACBA1271862997060E904720173430D1373A52DD4F8EB7E66A0D91DC5BB61B8879D2999AC9D5D56BBAE6B516851557856E67FEB3986DAC5C7814FFC34E6310368866251CEC9104A3B18E99F03AC465D166044CC3A7D49477302EC150C05B1D442BF1A28FA12E5CA70DE9C9B1B8643075FBB97B94D1DA83B3B93D03BAA81B25E41371F3A8E8C846B4EB28C6F33E06AF98805AECC026F0AF678B32BD0093B68C81BC94FBA87BFAE48B2A0A8A2CDDA9ACE4F17C764D44EA40C5A2C2B4F8EC695C372BE159E598A2C8AEC2A51503D1292AAACBE44036D29771BEC49995B080093CA934342431BF1CD50506D8CCC17A16D6F5CF215A4C94847A84CED526AF3F051326424A213F2C337AFEFE104AD9AEB23B64C768CDEADEDB8E65604035702B501514A1E9E3A4A11135BC9B08FB951290ED510BDB5216C5D7D75D85279BCB5C9891FAEE1610E9F9F780F6596253158456A3A2ABE91273295CBBEA32708EED3FA6995ADEEABA970C93FBEEB982B9B5309BDCBC9452BBB027D3A52320A5740A1CB4B4789C4C315436FB6A69F967073E580413D121D4941D85A4BC5F03FADB11164EAA356EEF495F1F7EEF74EB862ED2C905674FB2757797E13A48F9B2213D15C25E295FB84E8516729B687B19CAA8FF464C7A04E9DA5561B5C45529AC540389A93CD2E43113740411E55B49A7CC19D4E176DD67609A20A4A9A8F1E1B3E8B30844938DE3EFA3AF42E2E7D0E63F6971EBB71CC676AEBF77DAB468DD860E904720173430DBCBD79D6C764BCCFCA95C5801841FA1FE61B436BE3255FAB852B38F01CB274D8395DFDA55A967DE876CC69CD4C12BB3F775CDCBDC8FDD8723DD74045F61EF04FCC398D4487B1AF6F6DA255E837F41332D04D38092C99010BE4A4E5311542A294BE4C24A1C977C5DFDBFBEEF3B894984B607186CEAC7E678978ABBAE955D06AFFF930526A7FDD51CE052CE4735C5BBA9BB989544ACCC643EEFFA18C50C3A20DA074208BAE77E5DFB32FF5E55394661DB335C29D4EEAF134CB6B62A10E37101865EB456D29D275E7EA41C76897D63B854C35AC37943A13C95A40228A10781105D73EFA3AF42E2E7D0E63F6971EBB71CC672ACBA1271862997060E904720173430D5F756EA3BA2BEBD1CA95C5801841FA1F82D7B073F3E959EA852B38F01CB274D84D4BCCB8E22C9B175832759198715FB2F2D115816CBFA7D00AC0459C89D0640BDF4ACED620CB9C0100DA9C5093F88B8E3D80EF7B28B941A12E5E9C2E0164EE81E906A0B08D0060D58AA032C138799082B8B90F825BE43C3136576E08960AD236F80322311D677A81774C03898ECBE6589326AA26A04052A9B92C7FCBAB457AE70FC95D4C8B2FB790E6032E2CE2020DE55AFC1C29234EBF324B271C33EB6BD509221FD8B39C3D96389D893ED1C16A05B016E57550074A46E01B258FD83F01DFEA35E39F557D4AB03FD109C6C51C952C8E71071340870A68204CED526AF3F051326AF68722B4CB4C00D4351BF692066DCF4C768CDEADEDB8E62480477E25DAC88E9320A009BF68DF71303520EE0FCAF5C81ADB9A542F43DE9C50EB90EA4D6285FBC90649B3B7C6D4886E63F84BD5C3B02800DA9C5093F88B8EFCF8D35106404650776EDB026593A12DE906A0B08D0060D58AA032C138799082B8B90F825BE43C3136576E08960AD236F80322311D677A81774C03898ECBE658DB5A5948FA77AB29DFBA9CD1E45E47F901009658BF2BA41C5C3AF55B8812B20D914AF1DD54B32E6181C519C2A3A57D31221FD8B39C3D96385C0DE8006A3746AA673963F7A6B89C761B258FD83F01DFEA3E5771FB2CD4FD0E8E3DCAFA2DF9E0942E4B3AA14F1CD6EB7A379504C0E6053F74C12A66FDD16C85D4F3F332057D7BC0E6B4F295B031DDCC5B2D37B768B642E5BBAE6B51685155787A8AB1358E0474DB76CC69CD4C12BB3F775CDCBDC8FDD8723DD74045F61EF04FCC398D4487B1AF6F6DA255E837F41332D04D38092C99010BE4A4E5311542A294BE4C24A1C977C5DFDBFBEEF3B894984B607186CEAC7E678978ABBAE955D06AFF764DAB7BA56342F2A87E4C5E26F6417F2FF38E1C712CB147913204B91A4BC4942F1DC1A606D39DAEC2E912003020375B35C29D4EEAF134CB5C35A5BE151D63457569BC9295BECDC841C76897D63B854C8E987C13FD77DE0A6A18E0A56B17C0341E6BA40AA5864B04F0ED4485656EB3C509D95FA52A6BD54695DF1363F27C3139C6B5DF02F7DBF13165C34761531774E3D1242B45353F1E24242C2D48D4332F46189E16E7D9BF44FFF390EE556B4F9EAFA970AE4485387A0592E2D09731E9E5B881FD7D7C9EB716E66B54F9CF21C5D07D37D910E242E2D8D057F33947EB611EBCFC390E21DD58A87A0C5F1AC41A9CCAC23C956943DB8870F2EEEE686D36353EC9F4B198C8BDC376C7AD0146732580B9EBB0DC466722C70CB1CB580712A7524CE4F5B9D7D3755E43F24D65AD73B8CFF536EC19699E29F8A72949B314C35E48829B4E858D957D5D19133363D3A20110B9D9AD8A7B3ACDE3A9909B4DD6A9943FAFD90AE3BB6E13F6C4522AEDFA87745BBB86516E42A07AE3472C0394552C79E3436FAE4EE098938E896190B546F4807AE1AB978EA4C51DF121F7B85C73B0821A1D5B1414344B6A23DA9D3C67D3B1586D2E93051BD27FBDD38C8A21FB957B91771E3C58FCC869B420AE321617C00794C2795954A60A80AC29069389449B0B5A39F7E802FB360F336CD538F02AB8C1EC04F3DC42712B5CF43F06640417825079B49F6913341EB3E5CE8002B384945FE66450C7403B712FC7EBA2C66B70A16B0DDCD61AAE1B8D9A840C4F23F4C1930D9D5264397A4F4261A0F522D4E6704A3156C8402A4D33EA993BD9826D09DBA935A3D4A7DFAA58FFF3C9BBCC09D2B80AB5F8FEC2A3243968A9C1F0F28B6F40BF2132EFDE7D145E77329AA00976ED0494608FF68A15B3642D4E995EC47B216FD4921FCE07DA2DC2C7D40E152407411426CD3FC3F2484A1E9E3A4A11135BB2A633428A0E891D10BDB5216C5D7D751ED2B4A8C633CBD50922B412AA3A996F6596253158456A3A2ABE91273295CBBEA32708EED3FA6995682079F1402BB8D4EB982B9B5309BDCBC9452BBB027D3A52320A5740A1CB4B4789C4C315436FB6A69F967073E580413D121D4941D85A4BC519F0E4C8F8CE4C4EDD52689234C4E519E6356B857BBCD51FEAF43FE13E02CF852961DE444B45E0A5795E6B1A287556FAB19CAA8FF464C7A088A276736E332F9E9CE09216F7FDA03443113740411E55B47F4D925E710B20C3900389DCAA5171C04CED526AF3F05132306E5E5822F9F021B28C40A782F245E54C768CDEADEDB8E6FEF51659223AE42A9320A009BF68DF71A3B41229E6125CFB1ADB9A542F43DE9CBEC966B94A475E9F2B19E6DE57B808B66E63F84BD5C3B02800DA9C5093F88B8E3D80EF7B28B941A153B92101A86C3D59E906A0B08D0060D58AA032C138799082B8B90F825BE43C3136576E08960AD236F80322311D677A81FBB1F8E9721BA8B164A6B0F600AA0C7ED953995B4830D0B1E73C2F2A69B98831ECC703FCD7BC340BF870184E7AA567F102D568C30BF24C6F221FD8B39C3D96383EE94332F18EACB9673963F7A6B89C76EFEDBAF405F1DE254641C1C0E32FC17E2AEDFA87745BBB86AA7B40A11A320501E3C8C6D4FF24677FAE4EE098938E8961558F1FEBD2B831B8978EA4C51DF121F7D51872EAE042D4961414344B6A23DA9D3C67D3B1586D2E93051BD27FBDD38C8A5CE00D9E87FBFFC0D479F9550750196DA9D15AC2A0DCBA6AD7E05008BCEC6639CFB02431102EA046FF521FC20702CFE872CB066A4F8A8CB1088F012EE50056878EB94EB1D00883CF0D19C18369054DD5889FB8A1911989C125CDAE69F7C0D779E2819AB30AE0BC762DF05277815A457CD65374CB69510ADC8F8284180515BD04E92DBCF2B63BDD015B5D5159F6E13840C8FABB3A66750568289AAB4C2EFC6B3808626B1021AE08D718BACB874D418800ED0494608FF68A1527587C5546AD38585B3F58D3467EB88E2DC2C7D40E152407CD4AE3636BBDA1544A1E9E3A4A11135B5E175C29A287932310BDB5216C5D7D75CB1B00EB5DDF1E6D051BD27FBDD38C8A21FB957B91771E3C58FCC869B420AE321617C00794C2795954A60A80AC2906931D07F4526A48A2BC594A9C99831C2819F02AB8C1EC04F3DC42712B5CF43F06640417825079B49F6913341EB3E5CE8002B384945FE66450C7403B712FC7EBA2C628CDD461EF0C169AA6FAE6CC7E1B444974486489799ADC6D2F9B4F02E0481B3ED81081057F0C13A54D33EA993BD9826D09DBA935A3D4A7DF06A594948AD1B2B3D2B80AB5F8FEC2A375913640D62D19E20D423089A6577846963AB78001EF5A9B66AE4B7A25FE924D9553CA63A6C6491E7232BA9754A515C00D09681F439BF2C6DB66F77722232574C6755BDD6C5D73D8359B82BAB1E5334B20D3AB1ADB0C733B3A7EDA67227FB6889B02850CCBE67AC6B3D21F233744B1478FAEB3B93E89801254A60A80AC2906931D07F4526A48A2BC8A17FB39526F66C7F02AB8C1EC04F3DC42712B5CF43F06640417825079B49F6913341EB3E5CE8002B384945FE66450C7CB1244B01795D9E2D408BBDB9AA1A823FF95BF2BB75F51F12FB4C1AD4F6938C0BCFD6410B311CCF18E07DBE84AB2DA3D4D33EA993BD9826D09DBA935A3D4A7DF7F43C9124C8029D2D2B80AB5F8FEC2A34622ACEA31264943917F79F67889F9573E51D831062FF6644F188B618DE159574C4D51817317F3A5ED0494608FF68A157AA34AF5BED7163FEC4E7A9D8DC823F42DC2C7D40E152407000C1DE3513A5B2C4A1E9E3A4A11135BC9B08FB951290ED510BDB5216C5D7D75CA89DE7E8E74E7ADAEE1610E9F9F780F6596253158456A3A2ABE91273295CBBEA32708EED3FA699584EC7E6EF3594FB7EB982B9B5309BDCBC9452BBB027D3A52320A5740A1CB4B4789C4C315436FB6A69F967073E580413D121D4941D85A4BC5955DE71927689CE5438C0CA8BAD62FAD7479D7542045321E21DFB214A219DA27F2EC5277E86635FDCA7997A697B6463AB19CAA8FF464C7A03FEDE9EB41611A3473FACF5B8D67223143113740411E55B43083EEDA3A39790B714C8DD3A0C4A458201154FA531D6BAEED0494608FF68A15905FFA9B73D19B3302B90878DB222B172DC2C7D40E15240755C40669CE1BE87A4A1E9E3A4A11135B5E175C29A287932310BDB5216C5D7D75EC3AA59BE91D8DFF051BD27FBDD38C8A5CE00D9E87FBFFC0D479F9550750196DA9D15AC2A0DCBA6A6F32AF43DCA43B61CFB02431102EA046FF521FC20702CFE872CB066A4F8A8CB1088F012EE50056878EB94EB1D00883CF0D19C18369054DD52A05668D032A9750AB5CBF45EE3D184D8D8E511AF988B70E2AEF1A8806A67604917B178A2C971E4B7BD43894DABF1EBEE92DBCF2B63BDD016F4B846426C0E5CB5BA387EB5886B7F0289AAB4C2EFC6B38743F98846FBD459A49C806E69E661C25ED0494608FF68A1527587C5546AD38585B3F58D3467EB88E2DC2C7D40E1524075EF929C4EF04BD5D4A1E9E3A4A11135BC9B08FB951290ED510BDB5216C5D7D75CA89DE7E8E74E7AD0922B412AA3A996F6596253158456A3A2ABE91273295CBBEA32708EED3FA69958BC487250A8DACAAEB982B9B5309BDCBC9452BBB027D3A52320A5740A1CB4B4789C4C315436FB6A69F967073E580413D121D4941D85A4BC594CE9F1C5A55ABB9D20639697B73A678D608A7E999B77646585492E825581CD13580AD78D342B65DB5BF6EAE66313A2DB19CAA8FF464C7A01127E74C8A60CFFD9903D3153941C6B543113740411E55B4C4CCB51BF2CC54DB1623958C6B8355C3FC8E551A3F39B0D2AE7208271F504B1E9553CA63A6C6491EC53A6EC1C552382D282E2DAAE32A611E82F44FB2EF315E2FC58009E798106F31359B82BAB1E5334B800AD33CBE68ADDA7F1B9FC5D0D5EA429B02850CCBE67AC6B3D21F233744B1478FAEB3B93E89801254A60A80AC2906931D07F4526A48A2BC38B2FF3CE40A2FF8F02AB8C1EC04F3DC42712B5CF43F06640417825079B49F6913341EB3E5CE8002B384945FE66450C7403B712FC7EBA2C63331EB104F4CB29F7818AFEBCE7446F6BC1E12E83314A12DDD08A27CD791A5CE3975751AE945E5D84D33EA993BD9826D09DBA935A3D4A7DF9B04FCB428B8F8DED2B80AB5F8FEC2A3B0C6BEBBA0E368C7BB8E5B314CEE1A5D6945BA96646881150BF75996E0E955FD6DE9F973E60FBDE7E7AEEF70C4C098387C1CAD69A81EF2A42124F6B3AB41234013F883177BFDAA8A8BD4B35F05B3C4E05F01FEDB77BCF0FE189E16E7D9BF44FFB04D7739818FC95EA970AE4485387A0592E2D09731E9E5B85698665CDA33E85F209BF2B778D878F337D910E242E2D8D057F33947EB611EBCFC390E21DD58A87A0C5F1AC41A9CCAC23C956943DB8870F250D860C4D98F5F2CFCDCD5B4FE9C800B26A0AC1AFC012E3A4EFEAC021AD1D531783E1918593F756A683C829D1004C4244D65AD73B8CFF536EC19699E29F8A72977A03D3D960467114E858D957D5D191368DE5E8D2EB174F7013528B430DA37429D596181D6DD0CE05DA677693C69C671191898E47E8F66CAD8C4597C5CCEE6D61E6BA40AA5864B0406F50145ADF84F1D09D95FA52A6BD5468655A309C61C769F5CB472E835CC6FA9290FFF116223BBC2D1242B45353F1E2439397F97A7CE570B189E16E7D9BF44FFF390EE556B4F9EAFA970AE4485387A0592E2D09731E9E5B881FD7D7C9EB716E66B54F9CF21C5D07D37D910E242E2D8D057F33947EB611EBCFC390E21DD58A87A0C5F1AC41A9CCAC23C956943DB8870F250D860C4D98F5F2C5F71E04C18B850D37983C93F677C79BE0E2574FE8F1DD9892725B499BE47B5BD9AD42A0F2669E1A24D65AD73B8CFF536EC19699E29F8A72954ED73069BE6529C4E858D957D5D19130F552C5DB8B2F036D68F76BF4AC10182EE22B3CB25C545F31E6BA40AA5864B046B025EA0B146836709D95FA52A6BD546FBF59659A277824B9F455DD412EA9D12396A95EE69C4ED11D1242B45353F1E24A78E97CD6B257940C7814FFC34E6310330439EB0817B78A03B18E99F03AC465D166044CC3A7D494703EA95B06D4F899D0B962F0A57A5CAEE70DE9C9B1B8643075FBB97B94D1DA83B3B93D03BAA81B25E41371F3A8E8C846B4EB28C6F33E06AF98805AECC026F0AF69ED177A1D0D623AAAA6EC93F18BBFA62C1B3E4C8DC93883B7FB7C147FE007FC8FEF71667D9A4214472BE159E598A2C8AEC2A51503D1292AA9A5CEE7ECDF2197DEC49995B080093CAE8D79247AB2CAD3DD896555CC34C18673C600C8ACEC2A71CA3745D0EF27F72C34CED526AF3F051326AF68722B4CB4C00D4351BF692066DCF4C768CDEADEDB8E62C805EBF2ACCA6069320A009BF68DF71D496D3D6A2CD0DCC1ADB9A542F43DE9C9819C29FA63119ACC90649B3B7C6D4886E63F84BD5C3B02800DA9C5093F88B8EFCF8D35106404650776EDB026593A12DE906A0B08D0060D58AA032C138799082B8B90F825BE43C3136576E08960AD236F80322311D677A81774C03898ECBE65891585D94D6124BB834608F8F72EA006DB60346694C90283E67744BDFE32FBE2B60EA9A92D0F4C60768208743D19373253EAA1B01307012AA45E78C77ABF0841F9E3AF7DEC90888EC'

url = 'https://www.endata.com.cn/API/GetData.ashx'
headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '46',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'www.endata.com.cn',
    'Origin': 'https://www.endata.com.cn',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47',
    'X-Requested-With': 'XMLHttpRequest',
}
data = {
    'year': '2023',
    'MethodName': 'BoxOffice_GetYearInfoData',
}
da = requests.post(url=url, headers=headers, data=data).text
exc = execjs.compile(js).call('webInstace.shell', da)
exc = json.loads(exc)
pprint.pprint(exc)
