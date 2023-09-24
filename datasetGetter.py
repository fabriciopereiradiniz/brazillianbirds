from concurrent.futures import ThreadPoolExecutor
from bing_image_downloader import downloader

# Lista de parâmetros para cada chamada de download
downloads = [
    {"keyword": "Bem-te-vi pássaro", "output_dir": "Pitangus_sulphuratus"},
    {"keyword": "Pitangus sulphuratus", "output_dir": "Pitangus_sulphuratus"},

    {"keyword": "Sabiá-laranjeira pássaro", "output_dir": "Turdus_rufiventris"},
    {"keyword": "Turdus rufiventris", "output_dir": "Turdus_rufiventris"},

    {"keyword": "João-de-barro pássaro", "output_dir": "Furnarius_rufus"},
    {"keyword": "Furnarius rufus", "output_dir": "Furnarius_rufus"},

    {"keyword": "Canário-da-terra pássaro", "output_dir": "Sicalis_flaveola"},
    {"keyword": "Sicalis flaveola", "output_dir": "Sicalis_flaveola"},

    {"keyword": "Cardeal pássaro", "output_dir": "Paroaria_coronata"},
    {"keyword": "Paroaria coronata", "output_dir": "Paroaria_coronata"},

    {"keyword": "Tico-tico pássaro", "output_dir": "Zonotrichia_capensis"},
    {"keyword": "Zonotrichia capensis", "output_dir": "Zonotrichia_capensis"},
    
    {"keyword": "Rolinha-roxa pássaro", "output_dir": "Columbina_talpacoti"},
    {"keyword": "Columbina talpacoti", "output_dir": "Columbina_talpacoti"}
]

# Função para realizar o download
def do_download(params):
    downloader.download(params["keyword"], limit=1200, output_dir=params["output_dir"], adult_filter_off=True, force_replace=False, timeout=600)

# Criar um ThreadPoolExecutor com, por exemplo, 4 threads para downloads simultâneos
with ThreadPoolExecutor(max_workers=14) as executor:
    executor.map(do_download, downloads)

# Isso executará os downloads em paralelo com até 4 threads ao mesmo tempo.
