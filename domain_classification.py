import os
import glob

import os
import glob

# Dicionário expandido de categorias com pelo menos 100 palavras-chave associadas a cada uma
CATEGORIAS = {
    'ACESSO_REMOTO': ['teamviewer', 'anydesk', 'remote', 'vpn', 'rdp', 'logmein', 'vnc', 'ammyy', 'citrix', 'gotomypc', 
                      'gotomeeting', 'joinme', 'splash', 'remotix', 'connectwise', 'beyondtrust', 'supremo', 'remoteutilities',
                      'webex', 'remotepc', 'radmin', 'terminals', 'tmate', 'ultravnc', 'browsenext', 'netop', 'quicksupport',
                      'bomgar', 'realvnc', 'proviewer', 'chrome-remote-desktop', 'virtualdesktop', 'cloud-computer', 'cloudpc', 
                      'distant', 'remote-viewer', 'access', 'workfromhome', 'remoteconnection', 'virtual-machine', 'vworkspace',
                      'remoteconsole', 'desktop-sharing', 'virtualdesktop', 'computing', 'parallel', 'cloud', 'remoteanywhere', 
                      'virtual-desktop', 'parallel', 'vpn-access', 'rdp-remote', 'vdi', 'hostinger', 'cyberghost', 'shell', 
                      'msecure', 'strongdm', 'terminal', 'proxy', 'security', 'secureconnect', 'securedesktop', 'remoteadmin',
                      'freedesk', 'desktracker', 'guardremote', 'guarddesk', 'onlinedesk', 'desksupport', 'techsupport', 'itdesk', 
                      'remotejob', 'jobdesk', 'workdesk', 'openvpn', 'vpnunlimited', 'vpncity', 'gosecure', 'netsecure', 'appsec',
                      'zoomeye', 'vpn365', 'vpncontrol', 'proxynet', 'securenow', 'cyberdesk', 'cyberpc', 'geekconnect', 'hidemyip', 
                      'shieldconnect', 'connectedsecurity', 'accesspro', 'cloudshield', 'virtualaccess', 'rdpsecure', 'provirtual', 
                      'deskconnect', 'teamsconnect', 'accessanywhere', 'securedesk', 'itconnect'],
    
    'AMAZON': ['amazon', 'aws', 'prime', 'primevideo', 'kindle', 'audible', 'amazondeals', 'amazonwarehouse', 'amazonfresh', 
               'amazonmusic', 'amzn', 'amazonpay', 'alexa', 'echo', 'firetv', 'firestick', 'amazonservices', 'amazonshopping', 
               'amazongrocery', 'amazonsmile', 'amazonsupport', 'amazongames', 'amazonconnect', 'amazonnow', 'amazonprime', 
               'amazonseller', 'amazondeveloper', 'amazondrive', 'amazonsellercentral', 'amazonaffiliate', 'amazontv', 'amazonbooks',
               'amznw', 'amazonapp', 'amazonworkspaces', 'aws-support', 'awsiam', 'awss3', 'aws-amazon', 'awslambda', 'awscompute', 
               'awscloudfront', 'awscloud', 'awsdevops', 'awsconnect', 'awsmarketplace', 'amazonapps', 'amazonadvertising', 
               'amazonsupport', 'awsstorage', 'awsanalytics', 'awsapi', 'awsfinance', 'amazonhiring', 'amznjobs', 'amazonseller', 
               'amazonwebservices', 'amazonweb', 'awssecurity', 'awspayments', 'awsbilling', 'amazonjob', 'amazondelivery', 'amzgames', 
               'amzpay', 'amzonprime', 'amazonappstore', 'awsapp', 'awsdatabase', 'awsdynamodb', 'awsopensearch', 'awscloudservice', 
               'awscloudoperations', 'awsdocumentation', 'amazonprogram', 'amazon-smile', 'smileamazon', 'amazonhub', 'amazonpharmacy', 
               'amazonkids', 'amazonscholars', 'amazonmarket', 'amazonresearch', 'amazonwarehouse', 'amazonpublishing', 'awsdatasync', 
               'awsmigration', 'amzwork', 'amazontradein', 'awseducation', 'amazonadproducts', 'amzconnect', 'amzpartner', 'amzpublish'],

    'APLICACOES_EMPRESARIAIS': ['office365', 'zoom', 'slack', 'trello', 'microsoft', 'oracle', 'workday', 'jira', 'confluence',
                                'atlassian', 'asana', 'dropbox', 'salesforce', 'sap', 'zendesk', 'hubspot', 'paychex', 'service-now',
                                'docusign', 'quickbooks', 'ringcentral', 'adobe', 'gusto', 'intuit', 'workplace', 'webex', 'monday',
                                'spiceworks', 'marketo', 'spoke', 'xero', 'smartsheet', 'cisco', 'lucidchart', 'visio', 'powerbi',
                                'notion', 'clickup', 'bitrix', 'truedialog', 'doodle', 'tableau', 'sharepoint', 'zoominfo', 'sendgrid',
                                'sapconcur', 'gotomeeting', 'yammer', 'zenefits', 'bamboohr', 'freshbooks', 'expensify', 'tripactions',
                                'klaviyo', 'nextiva', 'basecamp', 'concur', 'synchronoss', 'autotask', 'clarizen', 'connectwise',
                                'tango', 'pipedrive', 'recruitee', 'pipefy', 'freshdesk', 'upwork', 'clickfunnels', 'todoist', 'gitlab',
                                'scoro', 'airtable', 'paypalbusiness', 'fieldglass', 'squarespace', 'wix', 'streak', 'amo', 'gustofx',
                                'hubstaff', 'sproutsocial', 'paylocity', 'planoly', 'kintone', 'workzone', 'highspot', 'tokbox', 'crowdcast',
                                'zoho', 'onehub', 'goodhire', 'workamajig', 'briteverify', 'hireology', 'upkeep', 'sherpany', 'bigin', 
                                'hubdoc', 'freshservice', 'teamviewerbusiness', 'goco', 'tsheets', 'birdeye', 'growbots', 'scorebuddy'],

    'APOSTAS': ['bet365', 'betfair', 'sportingbet', 'betway', '1xbet', 'betano', 'betsson', 'pokerstars', 'betclic', '888sport', 
                'williamhill', 'unibet', 'coral', 'ladbrokes', 'foxbet', 'casinoroom', 'lottomart', 'bovada', 'mybookie', 'betmgm', 
                'draftkings', 'fanduel', 'mohegan', 'goldennugget', 'sportsbet', 'mrgreen', 'redbet', 'royalvegas', 'intertops', 
                'sugarhouse', 'caesars', 'luxbet', 'dafu', 'bodog', 'spin', 'betsafe', 'vivogaming', 'grosvenorcasinos', 'betfred', 
                'matchbook', 'betstars', 'pointbet', 'kambi', 'scorebet', 'superbook', 'bravado', 'bigbetworld', 'superbet', 'solverde',
                'skyrise', 'betcart', 'beting', 'betonline', 'okex', 'betdaq', 'togel', 'jackpot', 'spinpalace', 'eurolotto', 'luckynugget', 
                'eclipsebet', 'venetianbet', 'casinoonline', 'betworld', 'slotocash', 'matchbets', 'mega', 'supabets', 'palmsbet', 'parimatch', 
                'wildcasino', 'bigwin', 'dafabet', 'betpro', 'playabets', 'fortuna', '888casino', 'casumo', 'betclub', 'slotsheaven', 'slotstars'],

    'ARMAZENAMENTO_EM_NUVEM': ['dropbox', 'googledrive', 'box', 'pcloud', 'icloud', 'meganz', 'oneDrive', 'backblaze', 'synology', 
                               'tresorit', 'spideroak', 'carbonite', 'opendrive', 'idrive', 'zoolz', 'justcloud', 'filecloud', 'owncloud', 
                               'rackspace', 'egnyte', 'bitcasa', 'securebackup', 'bigfile', 'wuala', 'hightail', 'mediafire', 'mozy', 
                               'elephantdrive', 'sugarsync', 'junocloud', 'sendspace', 'nextcloud', 'sharefile', 'cloudme', 'seafile', 
                               'nephoscale', 'minicloud', 'cubby', 'tardigrade', 'hubic', 'syncthing', 'memopal', 'drivesync', 'gdrive', 
                               'stack', 'filepicker', 'mimedia', 'boxcryptor', 'idisk', 'spacemonkey', 'fiicloud', 'yandexdisk', 'wasabi', 
                               'storj', 'filedropper', 'tactigon', 'rushfiles', 'centrestack', 'opencloud', 'azure', 's3storage', 'mozypro', 
                               'stronghold', 'gdrivepro', 'cleversafe', 'storagemadeeasy', 'silversky', 'securecloud', 'skydrive', 'cloudfiles', 
                               'livebook', 'fusecloud', 'backify', 'copy', 'xdrive', 'sparkleshare', 'jottacloud', 'unifyle', 'mymedia', 'datto', 
                               'livevault', 'ovhcloud', 'c2backup', 'fileder', 'scality', 'datahive', 'backupify', 'onedrive', 'storagedirect', 
                               'cloudpockets', 'skydrivepro', 'syncplicity', 'druva'],

    'BANKING': ['bankofamerica', 'chase', 'wellsfargo', 'citi', 'hsbc', 'barclays', 'santander', 'bbva', 'bancomer', 'boa', 'bancodoBrasil',
                'itau', 'bradesco', 'nubank', 'monzo', 'revolut', 'cashapp', 'venmo', 'sofi', 'capitalone', 'goldmansachs', 'jpmorgan',
                'citibank', 'alipay', 'paypal', 'rbc', 'tdbank', 'natwest', 'abnamro', 'ing', 'dbs', 'icicibank', 'hdfc', 'axisbank',
                'kotak', 'standardchartered', 'deutschebank', 'ubank', 'swedbank', 'nordea', 'firstdirect', 'allybank', 'charlesSchwab', 
                'usbank', 'pnc', 'citizensbank', 'morganstanley', 'ameritrade', 'rbs', 'yesbank', 'zelle', 'uobgroup', 'bankwest', 
                'anz', 'macquarie', 'commonwealth', 'scotiabank', 'bbt', 'bnymellon', 'ocbc', 'mufg', 'unibanco', 'banrisul', 'pagbank',
                'fidelity', 'leumi', 'svb', 'saxo', 'orangebank', 'bnpparibas', 'societegenerale', 'mebank', 'cibc', 'tangerine', 
                'vancity', 'kbc', 'eurobank', 'openbank', 'novobanco', 'santandertotta', 'easypaisa', 'bankia', 'fineco', 'lcl', 'posb', 
                'lombard', 'sydbank', 'vub', 'unicredit', 'maxbank', 'caja', 'oschadbank', 'privatbank', 'commerzbank', 'finserv', 'yapı', 
                'aktia', 'mtb', 'emporiki', 'garantibbva', 'nrwbank', 'swedbank', 'sbif', 'secbank', 'clbank'],

    'BATE_PAPO': ['whatsapp', 'telegram', 'signal', 'wechat', 'viber', 'facebookmessenger', 'line', 'kik', 'snapchat', 'discord', 'skype', 
                  'slack', 'mirc', 'icq', 'teamspeak', 'zalo', 'hike', 'threema', 'tango', 'imo', 'chathub', 'camfrog', 'yahooMessenger', 
                  'aol', 'omegle', 'tinychat', 'chatspin', 'twoo', 'kakaoTalk', 'paltalk', 'buzzarab', 'funchat', 'livechat', 'houseparty', 
                  'telegraph', 'trillian', 'chatiw', 'meetme', 'walkie', 'chatous', 'textnow', 'textme', 'messaging', 'groupme', 'frim', 
                  'penpal', 'chums', 'chatstep', 'e-chat', 'poparazzi', 'sup', 'ekko', 'strudel', 'wechatapp', 'textplus', 'lineapp', 
                  'textfree', 'jabber', 'zoosk', 'bodoo', 'icpb', 'pluschat', 'imlive', 'messageapp', 'goodnight', 'match', 'hookup', 
                  'bchat', 'sexchat', 'wink', 'badome', 'laytext', 'bbm', 'qoo', 'texty', 'opendm', 'hily', 'facechat', 'yabbie', 
                  'meetr', 'monkey', 'foov', 'matchmaker', 'toyboy', 'lovevox', 'firechat', 'omeet'],

    'BLOGS': ['wordpress', 'medium', 'tumblr', 'blogspot', 'weebly', 'ghost', 'typepad', 'squarespace', 'hubpages', 'livejournal', 
              'wix', 'blogger', 'myspace', 'xanga', 'gizmodo', 'engadget', 'arstechnica', 'boingboing', 'kottke', 'techcrunch', 
              'slashdot', 'bloglovin', 'bloggerapi', 'blogapp', 'blogging', 'googleblog', 'wordpressapp', 'microblogging', 'mediumapp',
              'instablog', 'postachio', 'contentful', 'pencilapp', 'blogly', 'thoughtcatalog', 'dailyblog', 'journ', 'posthaven', 
              'journalhome', 'blogaddict', 'paperr', 'problog', 'storychief', 'postpress', 'hexo', 'blogcast', 'scoopt', 'webblog', 
              'writeapp', 'tilda', 'weeb', 'weebon', 'postapp', 'hometown', 'bloggy', 'haiblog', 'miniblog', 'microblog', 'logbook', 
              'blurb', 'goodblog', 'upvote', 'storyblog', 'everblog', 'fixblog', 'writemore', 'blogcore', 'instablog', 'realblog', 
              'ezblog', 'bloghub', 'jotter', 'writerapp', 'bloggerapi', 'bitjournal', 'journalist', 'blogarchive', 'metablog', 
              'writersblock', 'letterly', 'logbook', 'earlyblog', 'snappyblog', 'dailyblog', 'yarnapp', 'tinyletter', 'blabber'],

    'BUSCADORES': ['google', 'bing', 'yahoo', 'baidu', 'duckduckgo', 'ask', 'aolsearch', 'yandex', 'lycos', 'excite', 'dogpile', 
                   'metacrawler', 'ecosia', 'startpage', 'qwant', 'gibiru', 'mojeek', 'search', 'searchengine', 'swisscows', 'wikipedia',
                   'bingsearch', 'searx', 'onesearch', 'vola', 'jive', 'xfinitysearch', 'securesearch', 'mypoints', 'engine', 'searchnow', 
                   'looksmart', 'tiscali', 'mozi', 'everlook', 'websearch', 'sosumi', 'mybrowser', 'opencrawl', 'fastbot', 'expanse', 
                   'smartlookup', 'searchface', 'trackthe', 'trackthis', 'cloudsearch', 'lucidworks', 'factbot', 'askbot', 'mommybot', 
                   'trecenti', 'backrub', 'webseeker', 'webcrawler', 'infoseek', 'botify', 'goodsearch', 'duckbot', 'surfbot', 'naver', 
                   'zocdoc', 'localbot', 'meatspace', 'mysearch', 'zibura', 'rotten', 'nodify', 'zenbot', 'startlookup', 'devlib', 
                   'goodsearch', 'myrobot', 'yourbot', 'andreas', 'yagoo', 'anybot', 'whoozi', 'indigo', 'idocbot', 'wayback', 
                   'netsearch', 'metabot', 'huri', 'topbot', 'botfinder', 'sopify', 'botfinder'],

    'DOWNLOADS': ['softpedia', 'cnet', 'sourceforge', 'tucows', 'uptodown', 'filehippo', 'softonic', 'freedownloadmanager', 'downloadcom', 
                  'portableapps', 'filehorse', 'getintopc', 'torrentz', 'warez', 'rapidshare', 'megashare', 'fileplanet', 'files', 
                  'mediafire', 'filerocket', 'down', 'downloadsite', 'installer', 'freeware', 'softwarefiles', 'cybershare', 'sharebytes', 
                  'fileshack', 'mega', 'shareware', 'stream', 'swfiles', 'superdownloads', 'freelibrary', 'softportal', 'filesave', 
                  'sites', 'zonefiles', 'storagehub', 'wefiles', 'streamhub', 'hubfiles', 'downloadfree', 'catalogue', 'appstore', 
                  'appdownloader', 'softpedia', 'filebulk', 'apphacks', 'freefiles', 'allfiles', 'dlsite', 'appfind', 'datahub', 
                  'hubstream', 'filesync', 'boxfiles', 'storehub', 'powerfile', 'appspot', 'cloudhub', 'dlfinder', 'drivehub', 'hubplus', 
                  'safedownload', 'quickfiles', 'filemaster', 'progfiles', 'totalshare', 'swissfiles', 'zfiles', 'dlzone', 'getfiles', 
                  'freebin', 'downloads', 'openfiles', 'filehub', 'bigfiles', 'uploadsite', 'hubspot', 'fastsite', 'dlcenter', 
                  'dlcloud', 'sourcedl', 'freedls'],

    'ECOMMERCES': ['amazon', 'ebay', 'aliexpress', 'etsy', 'rakuten', 'walmart', 'mercadolivre', 'shopee', 'flipkart', 'newegg', 'bigcommerce',
                   'target', 'bestbuy', 'wayfair', 'overstock', 'zalando', 'carrefour', 'shein', 'lazada', 'ikea', 'jd', 'macys', 
                   'costco', 'snapdeal', 'qvc', 'groupon', 'williams-sonoma', 'asda', 'homeDepot', 'lowes', 'kroger', 'boots', 
                   'wish', 'argos', 'tesco', 'aldi', 'shopify', 'toysrus', 'zappos', 'samsclub', 'hm', 'morrisons', 'jcpenney', 
                   'nordstrom', 'kohls', 'modcloth', 'bloomingdales', 'pier1', 'asos', 'hmart', 'bjs', 'rossstores', 'ultra', 
                   'havan', 'submarino', 'americanas', 'luizalabs', 'puntomio', 'casasbahia', 'extra', 'magazineluiza', 'dafiti', 
                   'netshoes', 'kanui', 'renner', 'ceacollection', 'fastshop', 'polishop', 'lojasamericanas', 'extra', 'pontoFrio', 
                   'centauro', 'cartier', 'louisvuitton', 'burberry', 'tiffany', 'fendi', 'chanel', 'gucci', 'prada', 'versace', 
                   'dolcegabbana', 'hollister', 'abercrombie', 'pacSun', 'sephora', 'bluefly', 'farfetch', 'sheinside', 'romwe', 
                   'prestashop', 'craigslist', 'dealnews', 'gearbest', 'asos'],

    'EDUCACAO': ['coursera', 'edx', 'udemy', 'khanacademy', 'academia', 'researchgate', 'quizlet', 'duolingo', 'babbel', 'memrise', 
                 'openai', 'wiley', 'pearson', 'studyblue', 'chegg', 'quizizz', 'schoology', 'mathway', 'brilliant', 'ted', 
                 'skillshare', 'codeacademy', 'scholar', 'socratic', 'unacademy', 'byjus', 'flipgrid', 'myopenmath', 'perusal', 
                 'knewton', 'edmodo', 'examprep', 'studocu', 'brightstorm', 'k12', 'alison', 'googleclassroom', 'learning', 
                 'bigideasmath', 'teacher', 'iteach', 'highschoolmath', 'university', 'ezschool', 'sparknotes', 'everfi', 
                 'brainly', 'highermathhelp', 'onlinelearning', 'classcentral', 'primaveraportal', 'khub', 'school', 
                 'teacherspayteachers', 'homeschooling', 'abcmouse', 'learningapps', 'scholarpedia', 'edhelper', 'study', 
                 'lumenlearning', 'cengage', 'studiesweekly', 'classdojo', 'mathbits', 'thinkwave', 'edulastic', 'skillsbuild', 
                 'digitalchalk', 'moodle', 'gutenberg', 'prodigygame', 'readworks', 'azlearning', 'epiklearning', 'rosenpublishing', 
                 'islearning', 'studyisland', 'khanlabs', 'acelearning', 'mathlearningcenter', 'toolboxtuesday', 'bookshare', 
                 'openstudy', 'webmath', 'sciencemath', 'phet', 'studyorg', 'noredink', 'discoveryschool', 'engrade', 'lms'],

    'ELETRONICOS': ['bestbuy', 'apple', 'samsung', 'sony', 'dell', 'lg', 'hp', 'acer', 'nvidia', 'intel', 'amd', 'gigabyte', 
                    'asus', 'lenovo', 'motorola', 'msi', 'toshiba', 'xbox', 'playstation', 'nintendo', 'garmin', 'dyson', 
                    'panasonic', 'seagate', 'logitech', 'fitbit', 'anker', 'alienware', 'huawei', 'vizio', 'pioneer', 'epson', 
                    'jabra', 'corsair', 'razer', 'roborock', 'blink', 'meizu', 'uniden', 'blackberry', 'oneplus', 'xiaomi', 
                    'sharp', 'sandisk', 'jbl', 'zebra', 'bose', 'tcl', 'roku', 'oppo', 'zte', 'polaroid', 'hyperx', 'viewsonic', 
                    'symantec', 'ibm', 'kaspersky', 'tp-link', 'trendmicro', 'legrand', 'ring', 'lacie', 'crucial', 'yubikey', 
                    'zagg', 'caseking', 'fujifilm', 'bosch', 'vtech', 'technicolor', 'blueiris', 'sonos', 'tplink', '3dconnexion', 
                    'targus', 'monoprice', 'tripplite', 'hikvision', 'avtech', 'zmodo', 'belkin', 'u-green', 'elgato', 'lacie', 
                    'vivint', 'koogeek', 'swann', 'supra', 'orus', 'mygica', 'alien'],

    'ESPORTE': ['espn', 'nbcsports', 'skysports', 'cbssports', 'fifa', 'nba', 'nfl', 'nhl', 'mlb', 'ufc', 'nascar', 'cricbuzz', 
                'tennis', 'golfdigest', 'bleacherreport', 'goal', 'sportsillustrated', 'athlete', 'marathon', 'running', 'track', 
                'field', 'sportsnet', 'boxingscene', 'mmafighting', 'jogoweb', 'cbf', 'swimming', 'cyclingnews', 'livescore', 
                'race', 'fitness', 'triathlon', 'workout', 'exercises', 'racechip', 'footy', 'sportscene', 'yogajournal', 
                'muscle', 'sportle', 'crossfit', 'training', 'snowboard', 'skateboard', 'parkour', 'rockclimbing', 'row2k', 
                'tabletennis', 'badminton', 'rugby', 'livesports', 'dazn', 'hiking', 'scouting', 'personaltraining', 'bootcamp', 
                'pilates', 'biathlon', 'archery', 'kayaking', 'raquetball', 'waterpolo', 'diving', 'outdoorsports', 'scorekeeper', 
                'simulator', 'bodysurf', 'champion', 'goalkeeper', 'handball', 'track', 'olympics', 'summitsports', 'swimsmooth', 
                'scuba', 'freedive', 'subnautica', 'teamusa', 'football', 'score', 'realfevr', 'flowmotion', 'goalnation', 
                'extreme', 'advancerunners', 'jujitsu', 'ringstar', 'shotokan', 'fishing'],

    'FILMES': ['imdb', 'rottentomatoes', 'letterboxd', 'fandango', 'filmweb', 'netflix', 'disneyplus', 'hulu', 'hbomax', 'primevideo', 
               'crunchyroll', 'amc', 'hbo', 'paramountplus', 'moviefone', 'cineplex', 'regmovies', 'filmschool', 'moviereview', 
               'movierank', 'allmovie', 'showtime', 'shudder', 'movieclips', 'amcnetworks', 'mubi', 'starz', 'screenrant', 
               'comingsoon', 'filmtrailer', 'movieinsider', 'boxoffice', 'indiewire', 'hollywoodreporter', 'variety', 'moviereel', 
               'filmaffinity', 'watch', 'docubase', 'documentary', 'filmhub', 'watchnow', 'screendaily', 'flick', 'moviepilot', 
               'rottent', 'cinemax', 'epix', 'tvtime', 'ifcfilms', 'cine', 'criterion', 'oscars', 'showbiz', 'goldenglobes', 
               'screenplay', 'moviethemes', 'boxd', 'actionfilm', 'drama', 'filmy', 'animation', 'horror', 'fantasyfilm', 
               'documentaries', 'romance', 'thriller', 'bollywood', 'marvel', 'dcfilms', 'universalpictures', 'dreamworks', 
               '20thcenturyfox', 'sony', 'warnerbros', 'mgm', 'lionsgate', 'solarmovies', 'movieflix', 'sflix', 'filmrise', 
               'vhx', 'moviez', 'stremio', 'azmovies', 'mymovie', 'mymovies', 'plex', 'tvseries', 'yts', 'yify', 'worldcinema', 
               'putlocker', '123movies', 'gostream', 'watchseries', 'dailymotion', 'flix', 'classicfilm', 'broadway', 'filmnoir'],

     'GOOGLE': ['google', 'gmail', 'googlemaps', 'googletranslate', 'googlephotos', 'googlecalendar', 'googledrive', 'googleads', 'googleanalytics', 
               'googlescholar', 'youtube', 'youtubemusic', 'googlesites', 'android', 'blogger', 'firebase', 'chromecast', 'doubleclick', 
               'googlecloud', 'googlepay', 'hangouts', 'googleplay', 'searchconsole', 'googleforms', 'gstatic', 'appspot', 'withgoogle', 
               'thinkwithgoogle', 'googlefonts', 'googlesurveys', 'googleearth', 'waze', 'g.co', 'madebygoogle', 'googlesupport', 'googleusercontent', 
               'googlestore', 'waymo', 'verily', 'deepmind', 'wing', 'stadia', 'projectfi', 'sidewalklabs', 'lookout', 'googleclassroom', 
               'dialogflow', 'googlemybusiness', 'thinkwithgoogle', 'learndigitalwithgoogle', 'googlekeep', 'google.org', 'googleforwork', 
               'abc.xyz', 'googlepartners', 'googleventures', 'googlecrisisresponse', 'admob', 'tensor', 'thinkwithgoogle', 'googlemarketing', 
               'googledev', 'googletravel', 'googleidentity', 'googleprivacy', 'googlenest', 'gsuite', 'googleblog', 'androiddev', 'developer.android'],

    'GOVERNO': ['gov', 'govuk', 'census', 'irs', 'ssa', 'uscis', 'nhs', 'epa', 'fda', 'govtrack', 'house', 'senate', 'treasury', 'dod', 
                'parliament', 'court', 'state', 'cia', 'nasa', 'usajobs', 'noaa', 'faa', 'cdc', 'justice', 'nps', 'governor', 'dot', 'omb', 
                'legis', 'police', 'customs', 'tax', 'congress', 'govt', 'secure', 'defense', 'dhs', 'gobierno', 'govbrazil', 'revenue', 
                'public', 'govonline', 'law', 'ombudsman', 'publicworks', 'postal', 'education', 'primeminister', 'govph', 'poderjudicial', 
                'govin', 'govng', 'gob', 'govindonesia', 'govus', 'govgr', 'govau', 'gov.sg', 'mod', 'gov.cy', 'govil', 'gouv', 'defra', 
                'govco', 'govjo', 'govqa', 'govpk', 'gofreight', 'govru', 'govae', 'govkp', 'gov.uk', 'nordgov', 'government.nl'],

    'HUMOR': ['9gag', 'memedroid', 'iFunny', 'failblog', 'funnyordie', 'chive', 'memecenter', 'humor', 'lol', 'cracked', 'damnlol', 
              'imgflip', 'memes', 'quickmeme', 'smosh', 'buzzfeed', 'cheezburger', 'xkcd', 'funnyjunk', 'jokes', 'textpost', 'memebase', 
              'memes.com', 'comedy', 'funniest', 'laugh', 'sarcasm', '4chan', 'lolsnaps', 'memehub', 'funnyvote', 'reddit_funny', 
              'memez', 'viral', 'collegehumor', 'thelaughbutton', 'thepoke', 'epicfails', 'memepool', 'laughfactory', 'babyyoda', 
              'wearethememes', 'laughoutloud', 'wholesomememes', 'pepethefrog', 'dankmemes', 'stolenmemes', 'funnypictures', 'totallylookslike', 
              'memewar', 'toomanyfunny', 'epicmeme', 'meming', 'memeupdate', 'funnytext', 'makeameme', 'memeking', 'laughbite', 'saturdayfun'],

    'INTELIGENCIA_ARTIFICIAL': ['openai', 'chatgpt', 'bard', 'midjourney', 'stability', 'huggingface', 'cohere', 'anthropic', 'inflection', 
                                'runway', 'neuralink', 'deepmind', 'nvidiaai', 'watson', 'alibabaai', 'microsoftai', 'faceplusplus', 
                                'clarifai', 'voicera', 'speechmatics', 'awsml', 'azureml', 'vertexai', 'ibmcloudai', 'salesforceeinstein', 
                                'ai21', 'abbyy', 'kapwing', 'jasperai', 'snorkel', 'synthesia', 'openmind', 'braincorp', 'cleverbot', 
                                'replika', 'voiceai', 'datadogai', 'domoai', 'contentdna', 'aigenerations', 'playgroundai', 'artbreeder', 
                                'deepai', 'aiassistant', 'weaviate', 'deeplearning', 'machinelearning', 'finetuning', 'predict', 
                                'automl', 'deepturing', 'elementai', 'computervision', 'cognitiveservices', 'recurrent', 'embeddings', 
                                'deepface', 'xnor', 'modeling', 'extraction', 'bigml', 'algorithms', 'machinevision', 'bigbrain', 'deepr'],

    'JOGOS': ['steam', 'epicgames', 'ubisoft', 'playstation', 'xbox', 'nintendo', 'ea', 'riotgames', 'roblox', 'twitch', 'discord', 
              'gog', 'battlenet', 'gamespot', 'kotaku', 'minecraft', 'fortnite', 'wow', 'gamefaqs', 'esl', 'ign', 'pcgamer', 
              'nvidia', 'gamepass', 'thesims', 'pokemongo', 'gameplay', 'espn_esports', 'crossfire', 'warframe', 'gamepedia', 
              'pubg', 'valorant', 'leagueoflegends', 'dota2', 'callofduty', 'battlefield', 'csgo', 'amongus', 'apexlegends', 
              'fallguys', 'cyberpunk', 'fifa', 'madden', 'destiny', 'borderlands', 'clashofclans', 'candycrush', 'rocketleague', 
              'guildwars', 'runescape', 'halo', 'elder', 'finalfantasy', 'tekken', 'streetfighter', 'mortalcombat', 'ghostrecon', 
              'assassinscreed', 'granblue', 'smashbros', 'dungeonsdragons', 'overwatch', 'yugioh', 'pokemontcg', 'hearthstone', 
              'wowclassic', 'genshinimpact', 'totalwar', 'play', 'retro', 'sims'],

    'MICROSOFT': ['microsoft', 'windows', 'office', 'onedrive', 'outlook', 'skype', 'msn', 'bing', 'xbox', 'azures', 'microsoftteams', 
                  'github', 'linkedin', 'msdn', 'powerbi', 'dynamics', 'microsoftstore', 'yammer', 'mix', 'hololens', 'microsoft365', 
                  'live', 'sharepoint', 'microsoftedge', 'ie', 'visualstudio', 'powerpoint', 'excel', 'word', 'access', 'onedrive', 
                  'mspoweruser', 'techcommunity', 'msoutlook', 'technet', 'docs.microsoft', 'dotnet', 'msazure', 'surface', 'infopath', 
                  'microsoftgraph', 'msoffice', 'msdn.microsoft', 'msstore', 'msonline', 'msevent', 'microsoftdeveloper', 'exchange', 
                  'msonline', 'azuredev', 'windowsserver', 'winbeta', 'msbuild', 'microsoftgames', 'msstore', 'msmixer', 'msvisio'],

    'MUSICAS': ['spotify', 'soundcloud', 'applemusic', 'deezer', 'tidal', 'pandora', 'bandcamp', 'lastfm', 'audiomack', 'reverbnation', 
                'shazam', 'iheart', 'mixcloud', 'jiosaavn', 'beatport', 'audiomack', 'musictimes', 'genius', 'azlyrics', 'musixmatch', 
                'livexlive', 'vinylmeplease', 'classicalfm', 'radiotunes', 'allmusic', 'digitalsound', 'smule', 'idolator', 'gaana', 
                'myspace', 'soundhound', 'soundclick', 'freegalmusic', 'songkick', 'concert', 'gigfinder', 'spotalike', 'lyricstranslate', 
                'musicto', 'amazonmusic', 'rhapsody', 'freesound', 'jazzradio', 'rap', 'trending', 'musicfox', 'emusic', 'musicfrom', 
                'liveradio', 'tuneinradio', 'internet-radio', 'guitarhero', 'coke', 'country', 'sound', 'pop', 'gospel', 'jazz', 'classical', 
                'hiphop', 'blues', 'metal', 'rock', 'electronic', 'folk', 'instrumental'],

    'P2P_TORRENT': ['torrent', 'thepiratebay', '1337x', 'rarbg', 'yts', 'kickass', 'extratorrent', 'limetorrents', 'zooqle', 'torrentz', 
                    'torlock', 'seedpeer', 'bitsnoop', 'demonoid', 'torrentdownloads', 'monova', 'idopese', 'bt-scene', 'ettv', 'kat', 
                    'moviepedia', 'torrentfunk', 'toros', 'yourbittorrent', 'torrentproject', 'bittorrent', 'tracker', 'openbittorrent', 
                    'mininova', 'sharetv', 'moviemagnet', 'magnetdl', 'isoHunt', 'rarbgmirror', 'megaupload', 'filehost', 'torrentfiles', 
                    'torrenthound', 'torrentdb', 'btarena', 'freetorrent', 'torrentking', 'torrentree', 'extratorrents', 'exvagos', 
                    'kickasskat', 'torrent-room', 'torrentcounter', 'rarbggo'],

    'PORNOGRAFIA': ['pornhub', 'xvideos', 'xnxx', 'chaturbate', 'brazzer', 'onlyfans', 'livejasmin', 'cam4', 'camsoda', 'stripchat', 
                    'camwhores', 'youporn', 'redtube', 'spankbang', 'tnaflix', 'lust', 'rule34', 'tube8', 'xtube', 'faphouse', 'erome', 
                    'slutload', 'xhamster', 'cams', 'mature', 'jizzbunker', 'pornmd', 'pornhd', 'babes', 'fantasy', 'milf', 'kink', 'playboy', 
                    'bangbros', 'realitykings', 'bad-dragon', 'clips4sale', 'myfreecams', 'camsoda', 'filth', 'amateur', 'hot', 'dare', 
                    'blow', 'chat', 'fetish', 'fet', 'hub', 'matureporn', 'tiny', 'camsfuse', 'exotic', 'wet', 'bad', 'camstube'],

    'PORTAIS': ['uol', 'terra', 'ig', 'r7', 'bol', 'globo', 'yahoo', 'msn', 'reddit', 'flipboard', 'buzzfeed', 'digg', 'vib', 'dailynews', 
                'usatoday', 'eltiempo', 'elpais', 'lemonde', 'bbc', 'apnews', 'cnnbrasil', 'abcnews', 'forbes', 'bloomberg', 'financialtimes', 
                'boston', 'aljazeera', 'npr', 'independent', 'buzz', 'telegraph', 'guardian', 'timesofindia', 'straitstimes', 'washingtonpost', 
                'thesun', 'chicagotribune', 'usatoday', 'express', 'metro', 'observer', 'nytimes', 'politico', 'axios', 'detroitnews', 
                'wpost', 'sfgate', 'usmagazine', 'slate', 'dailykos', 'bostonglobe', 'dailymirror', 'dailymail', 'tribune'],

        'REDE_SOCIAIS': ['facebook', 'instagram', 'twitter', 'tiktok', 'snapchat', 'whatsapp', 'wechat', 'linkedin', 'telegram', 
                     'pinterest', 'tumblr', 'reddit', 'flickr', 'vine', 'periscope', 'myspace', 'friendster', 'bebo', 'mewe', 
                     'kakaotalk', 'line', 'vkontakte', 'qq', 'mixi', 'peach', 'nextdoor', 'viber', 'wechat', 'plurk', 'mastodon', 
                     'gab', 'clouthub', 'parler', 'getter', 'clubhouse', 'taringa', 'ello', 'diaspora', 'couchsurfing', 'goodreads', 
                     'ok.ru', 'medium', 'livejournal', 'weibo', 'renren', 'snap', 'onlyfans', 'discord', 'messenger'],

    'STREAMING': ['netflix', 'primevideo', 'hulu', 'disneyplus', 'hbomax', 'crunchyroll', 'funimation', 'peacocktv', 'fubo', 'sling', 
                  'dazn', 'showtime', 'starz', 'pandora', 'spotify', 'deezer', 'soundcloud', 'applemusic', 'tidal', 'youtubemusic', 
                  'napster', 'audible', 'paramountplus', 'iplayer', 'iplayer', 'pluto.tv', 'tubitv', 'mxplayer', 'jiotv', 'gaana', 
                  'tvnow', 'plex', 'kanopy', 'mubi', 'discoveryplus', 'shahid', 'iflix', 'sonyliv', 'aha', 'viu', 'hotstar', 'zee5', 
                  'hbo', 'rokutv', 'puhu', 'viki', 'joox', 'patreon', 'quibi', 'vimeo', 'ustream'],

    'SHOPPING': ['amazon', 'alibaba', 'aliexpress', 'ebay', 'mercadolivre', 'etsy', 'rakuten', 'bestbuy', 'walmart', 'wish', 'shopee', 
                 'carrefour', 'costco', 'target', 'home', 'ikea', 'weg', 'samsclub', 'newegg', 'bhphotovideo', 'argom', 'flipkart', 
                 'daraz', 'groupon', 'shop', 'deal', 'emart', 'zalando', 'next', 'asos', 'overstock', 'qvc', 'gnc', 'bookdepository', 
                 'bookshop', 'myntra', 'farfetch', 'sephora', 'ulta', 'flipkart', 'grofers', 'ubuy', 'bigbasket', 'snapdeal', 
                 'snapfish', 'sclick', 'targetplus', 'tops'],

    'NOTICIAS': ['cnn', 'bbc', 'nytimes', 'wsj', 'forbes', 'reuters', 'bloomberg', 'usatoday', 'cbsnews', 'abcnews', 'aljazeera', 
                 'foxnews', 'npr', 'msnbc', 'washingtonpost', 'latimes', 'newsweek', 'time', 'huffpost', 'guardian', 'newsmax', 
                 'businessinsider', 'rt', 'univision', 'telemundo', 'elpais', 'lefigaro', 'lemonde', 'dailymail', 'thesun', 
                 'financialtimes', 'newyorker', 'axios', 'buzzfeed', 'flipboard', 'infobae', 'timesofindia', 'globoesporte', 
                 'g1', 'oantagonista', 'em.com', 'correiobraziliense', 'estadão', 'veja', 'valor', 'band', 'recordtv', 'ndtv'],

    'EDUCACIONAL': ['coursera', 'edx', 'udemy', 'khanacademy', 'futurelearn', 'udacity', 'alison', 'codeacademy', 'openlearn', 
                    'w3schools', 'linkedinlearning', 'brilliant', 'pluralsight', 'skillshare', 'datacamp', 'lynda', 'memrise', 
                    'duolingo', 'babbel', 'rosedale', 'byjus', 'vedantu', 'unacademy', 'icai', 'bytedance', 'turing', 'stepik', 
                    'hellotalk', 'sololearn', 'accredible', 'thinkific', 'vivedu', 'elearning', 'openlearning', 'openclassrooms', 
                    'quizlet', 'teachabl', 'treehouse', 'blockacademy', 'alamance', 'academic', 'academicresource'],

         'RESTRICOES_PROCON': ['jogo', 'bet365', 'pokerstars', 'betfair', '888casino', 'blaze', 'leovegas', '1xbet', 'williamhill', 'betway', 
                          'sportingbet', 'bwin', 'betsson', 'betano', '22bet', 'rivalo', 'bodog', 'jackpot', 'luckia', 'casino', 
                          'bingoonline', 'slotomania', 'megajogos', 'freespin', 'blackjack', 'ladbrokes', 'unibet', 'betclic', 'royalvegas', 
                          'casumo', 'betvictor', 'paddypower', 'mrgreen', 'gala', 'betfred', 'superbahis', 'codere', 'interwetten', 'bingo', 
                          'spin', 'jackpotcity', 'slotland', 'gamblers', 'jogodebicho', 'scasino', 'gamevance', 'betboo', 'casinotitan', 
                          '24hrsbets', 'apostaganh', 'easybet', 'azartmania', 'freelotto', 'starcity'],

    'SERVIDORES_ADSENSE': ['doubleclick', 'googlesyndication', 'adservice', 'adsense', 'media.net', 'criteo', 'outbrain', 'taboola', 
                           'revcontent', 'mgid', 'adroll', 'clickadu', 'propellerads', 'zedo', 'yahoo', 'rubiconproject', 'appnexus', 
                           'pubmatic', 'openx', 'adcolony', 'smaato', 'bidtellect', 'sonobi', 'contextweb', 'indexexchange', 'triplelift', 
                           'spotx', 'bidswitch', 'rhythmone', 'gumgum', 'yahoossp', 'smartadserver', 'teads', 'kargo', 'moat', 
                           'stickyadstv', 'xandr', 'simplifi', 'mediavine', 'brid', 'undertone', 'chitika', 'verizonmedia', 'quantcast', 
                           'geniusmonkey', 'zergnet', 'stackadapt', 'content.ad', 'taboola', 'insticator', 'sovrn', 'exponential', 
                           'pulsepoint', 'nativo', 'revive', 'bidsmart', 'clickio', 'marfeel', 'yieldmo'],

    'STREAMING': ['netflix', 'primevideo', 'disneyplus', 'hulu', 'hbomax', 'paramountplus', 'twitch', 'youtube', 'spotify', 'applemusic', 
                  'soundcloud', 'deezer', 'tidal', 'pandora', 'crunchyroll', 'funimation', 'viki', 'peacocktv', 'pluto.tv', 'sling', 
                  'xumo', 'dazn', 'fubo', 'showtime', 'starz', 'quibi', 'mubi', 'ustvgo', 'jiocinema', 'hotstar', 'tvnow', 'plex', 
                  'roku', 'voot', 'sonyliv', 'viutv', 'iflix', 'shahid', 'kanopy', 'livestream', 'youtubetv', 'boxplus', 'wowza', 
                  'ustream', 'ustvnow', 'bein', 'discoveryplus', 'fancast', 'gaana', 'joox', 'rokuchannel', 'cbsallaccess', 'radiotime', 
                  'buzzr', 'afizz'],

    # Adicione mais categorias, se necessário
}
                      
# Função de classificação aprimorada
def classificar_dominio(dominio):
    for categoria, keywords in CATEGORIAS.items():
        if any(keyword in dominio.lower() for keyword in keywords):
            return categoria
    return 'OUTROS'

# Função para processar os arquivos no diretório
def processar_arquivos(diretorio):
    # Procurar arquivos que começam com "cloudflare-radar_top-5000-domains"
    arquivos = glob.glob(os.path.join(diretorio, 'cloudflare-radar_top-5000-domains*'))

    for arquivo in arquivos:
        # Verificar se o arquivo é do tipo esperado
        if arquivo.endswith('.csv') or arquivo.endswith('.txt'):
            print(f"Processando arquivo: {arquivo}")
            
            # Ler o arquivo e classificar os domínios
            with open(arquivo, 'r') as f:
                dominios = f.readlines()

            # Classificar cada domínio
            classificacoes = {dominio.strip(): classificar_dominio(dominio.strip()) for dominio in dominios}

            # Salvar o resultado em um novo arquivo
            nome_arquivo_saida = arquivo.replace('cloudflare-radar_top-5000-domains', 'classificados_cloudflare')
            with open(nome_arquivo_saida, 'w') as f_out:
                for dominio, categoria in classificacoes.items():
                    f_out.write(f"{dominio}, {categoria}\n")
            
            print(f"Classificação salva em: {nome_arquivo_saida}")

# Função principal
def main():
    # Diretório onde os arquivos estão localizados  
    diretorio = '/home/alisson/group_generator_rules'

    # Processar os arquivos no diretório especificado
    processar_arquivos(diretorio)

if __name__ == "__main__":
    main()
