from twitter import *

# install with: pip install twitter
# Create new app and access token from https://apps.twitter.com/

token = ''
token_secret = ''

consumer_key = ''
consumer_secret = ''

chunk_size = 20


tw = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

screen_name = 'iEx_ec,LunyrInc,DECENTplatform,musicoins,CoinMagi,augurproject,LiskHQ,dogecoin,monerocurrency,Ripple,Dashpay,omise_go,neo_blockchain,tenxwallet,tokesplatform,WavesPlatform,IncentLoyalty,KomodoPlatform,tokencard_io,monaco_card,eboostcoin,geo_coin,Crowncoin1,MonetaryUnit,ionomics,Golos_Gold,goloschain,ubiqsmart,QtumOfficial,DECENTplatform,bancornetwork,FunFairTech,NxtCommunity,golemproject,wingsplatform,ArkEcosystem,_pivx,vergecurrency,ArdorPlatform,AdEx_Network,AragonProject,civickey,firstbloodio,darcrus,gnosisPM,EOS_io,2givecoin,ad_chain,apx_ventures,officialaur,AttentionToken,BitBayofficial,bitcolncash,BitBeanCoin,bitalize,coinblack,the_blocknet,ArtByteMe,aeoncoin,synereo,spellsofgenesis,breakoutcoin,bit_send,breakoutgaming,bata_money,bitcoindark,bitshares,burstcoin_dev,bytecent_byc,cannabiscoins,cofound_it,clamclient,cloakcoin,clubcoin_co,circuitsofvalue,creditbit,CapriCoinTeam,curecoin_team,decredproject,digibytecoin,digixdao,digixglobal,dgxio,dmdcoin,dopecoingold,E_Drachma,augmentorsgame,dualitychain,edgelessproject,elecgulden,evergreencoin_,emercoin,einsteiniumcoin,energycoin,europecoineuorg,eth_classic,ethereumproject,exclusivecoin,expanseofficial,faircointeam,fair_coop,factom,foldingcoin,official_florin,feathercoin,gambitcrypto,gamecredits,byteballorg,gcrworldwide,goldcoin,gridcoinnetwork,groestlcointeam,matchpool,Humaniq,infxcoin,io_coin,Fermat_ORG,newkorecoin,lbryio,legendsroom,coinlomo,litecoin,maidsafe,pepecoins,melonport,metalpaysme,mysteriumnet,navcoin,officialnubits,neoscoin,gulden,numerai,BeyondVoidGame,nxsearth,okcashcrypto,omni_layer,particlproject,ParticlDev,pinkcoin_,parkbyte_pkb,potcoin,peercoinppc,pesetacoinofic,patientory,qrledger,qwarktoken,radiumcore,rubycoinorg,reddcoin,risevisionteam,safe_Exchange,siatechhq,dualitychain,ShiftNrg,sibchervonec,solarcoin_slr,singulardtv,synergycoin,ethstatus,ProjectSPHR,spreadcointeam,start_coin,StartJOIN,Startwallet,steemit,steemchain,storjproject,stratisplatform,bit_swift,swarmcitydapp,syndicatelabs_,syscoin,thehempcoin,chronobanknews,blocksafe,wetrustplatform,trustplus,transfer_dev,unbreakablcoin,unobtanium_uno,viacoin,voxelus,vericoin,veriumreserve,Vertcoin,vtorrentcrypto,urumproject,XaurumOfficial,counterpartyxcp,digitalnote_xdn,elastic_coin,NEMofficial,stellarorg,myriadcoin,stealthcoin,xvcnews,whitecoiner,zcoinofficial,zcoinproject,zclassiccoin,zcashco,zencashofficial'
screen_name = screen_name.split(',')
for i in range(len(screen_name))[::chunk_size]:
    # split to chunk size
    sn = ','.join(screen_name[i:i+chunk_size])
    tw.lists.members.create_all(
        owner_screen_name='your_screen_name_here', slug='your_list', screen_name=sn)
