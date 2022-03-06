def GardenQuery(wallet_addr):
    from web3 import Web3, HTTPProvider
    import math, time
    from datetime import datetime

    contract_address = Web3.toChecksumAddress("0x685bfdd3c2937744c13d7de0821c83191e3027ff")
    contract_abi = '[{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"hatcheryPlants","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"getUserSeeds","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"SEEDS_TO_GROW_1PLANT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
    web3 = Web3(HTTPProvider("https://bsc-dataseed.binance.org:443"))
    myContract = web3.eth.contract(address=contract_address, abi=contract_abi)

    getUserPlants = myContract.functions.hatcheryPlants(wallet_addr).call()
    getSeedsPerPlant = myContract.functions.SEEDS_TO_GROW_1PLANT().call()
    getUserSeeds = myContract.functions.getUserSeeds(wallet_addr).call()
    seedsPerDay=getUserPlants*86400
    seedsPerSecond=seedsPerDay/24/60/60
    secondsUntilNextPlant=(getSeedsPerPlant-(getUserSeeds%getSeedsPerPlant))/seedsPerSecond
    print("|| "+wallet_addr+" || " + str(datetime.now()))
    print("Plants total: "+str(getUserPlants) \
        +" | New plants ready: "+str(math.floor(getUserSeeds/getSeedsPerPlant))
        +" | Seeds total: "+ str(getUserSeeds)
        +" | Minutes per Plant: "+str(round(getSeedsPerPlant/(seedsPerSecond*60),2))
        +" | Next Plant ETA: "+str(int(round(secondsUntilNextPlant)))+" seconds")
    print()

    print("Waiting "+str(int(round(secondsUntilNextPlant)))+" seconds until the next plant is complete")
    time.sleep(secondsUntilNextPlant+0.1)

    #Do something - Play a sound or trigger a transaction
    import winsound
    for i in range(1, 3):
        winsound.Beep(i * 300, 150)

GardenQuery("0x4532BBeA6EC2Df2b914df9c3f03D1D19F30701b1")
