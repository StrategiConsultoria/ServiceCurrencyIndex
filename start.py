from server.scrape import RunningScrape
from server.scrape.ipeadata import IpeadataScrape
from pprint import pprint
import json

run = RunningScrape()

ipca = IpeadataScrape(38391)
run.join(ipca, 'ipca')

incc = IpeadataScrape(33596)
run.join(incc, 'incc')

igpm = IpeadataScrape(37796)
run.join(igpm, 'igpm')

with open('out.json','w') as file:
    file.write(json.dumps(run.start()))