from subprocess import run
import json
import os


async def command(serid:int) -> list:
    """call the collect with scrapy in cmd
    
    :entry:
        :serid: int
    :return:
        list -> [{'date':str,'index':str}]
    """
    output_file = f'{serid}.json'
    if os.path.isfile(output_file):
        os.remove(output_file)
    run(['scrapy', 'crawl', 'collect', '-a',
        f'serid={serid}', '-O', output_file])
    with open(output_file) as file:
        data = json.loads(file.read())
    os.remove(output_file)
    return data
