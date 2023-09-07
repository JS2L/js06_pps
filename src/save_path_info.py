import os
import pandas as pd
# import js06_log

save_path = os.path.join("C:/path_info")
file_path = os.path.join(f"{save_path}/path_info.csv")    
# logger = js06_log.CreateLogger(__name__)

def init_data_path():
    
    try:
        os.makedirs(f"{save_path}")
        print("Initialization path settings")
    except Exception as e:
        pass
    
    data_path = [('C:/data', 'C:/images', 'C:/log', '192.168.100.132')]
    
    cols = ['data_path', 'image_path', 'log_path', 'camera_ip_path']
    path_info_df = pd.DataFrame(data_path, columns=cols)
    
    path_info_df.to_csv(file_path, mode="w", index=True)
    
    # logger.info("Initialization path settings")

def get_data_path(path_name):
    
    try:
        path_df = pd.read_csv(file_path)    
    
    except Exception as e:
        init_data_path()
        path_df = pd.read_csv(file_path)        
        
    get_text = path_df.loc[0,path_name]
    
    # logger.info(f'Get {path_name} value')
    return get_text


def set_data_path(path_name, new_folder_path):    
    
    path_df = pd.read_csv(file_path)
    
    old_folder_path = path_df.loc[0, path_name]
    path_df = path_df.replace({path_name: old_folder_path}, {path_name: new_folder_path})
    
    path_df.to_csv(file_path, mode="w", index=False)
    
    
        
    
    
    
    
    
    