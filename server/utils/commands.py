from subprocess import run
import json
import os


async def command(serid, output_file) -> list:
    """call the collect with scrapy in cmd"""
    run(['scrapy', 'crawl', 'collect', '-a',
        f'serid={serid}', '-O', output_file])
    with open(output_file) as file:
        data = json.loads(file.read())
    os.remove(output_file)
    return data


async def update_ipca(output_file='ipca.json') -> list:
    """call the collect to ipca"""
    return await command(38391, output_file)


async def update_incc(output_file='incc.json') -> list:
    """call the collect to incc"""
    return await command(33596, output_file)


async def update_igpm(output_file='igpm.json') -> list:
    """call the collect to igpm"""
    return await command(37796, output_file)
