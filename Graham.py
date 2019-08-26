def isBonusSuccessive(tick,begin,end=u''):
    bonuses=DataAPI.EquDivGet(secID=u"",ticker=tick,beginDate=begin,endDate=end,beginPublishDate=u"",endPublishDate=u"",beginRecordDate=u"",endRecordDate=u"",field=u"",pandas="1")
    #print bonuses
    years=set()
    for index, row in bonuses.iterrows():
        if row['perCashDiv']>0.0 or row['perShareDivRatio'] or row['perShareTransRatio'] :
            years.add(row['endDate'][:4])
    #print row["perCashDiv"], row["payCashDate"]
    if len(years)>18:
        return True
    else:
        return False
    #print(len(years))
testdate=u"20190816"
data=DataAPI.MktEqudGet(secID=u"",ticker=u"",tradeDate=testdate,beginDate=u"",endDate=u"",isOpen="",field=u"",pandas="1").sort(["marketValue"],ascending=False)
length=len(data)*5//100
maxCompanies=data.head(length)
blueCompanies=maxCompanies[maxCompanies.PE<25]
#print(blueCompanies[['ticker','secShortName','marketValue','PE']])
for index,row in blueCompanies.iterrows():
    if isBonusSuccessive(row['ticker'],u'19990101',testdate):
        print(row['ticker']),row['secShortName'],row['closePrice'],row['PE'],row['marketValue']
