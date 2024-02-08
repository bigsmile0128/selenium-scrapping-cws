import os


# data root dir path
ranking_data_path = os.path.join('data', 'ranking')

# result_list dir path
result_list_save_path = os.path.join(ranking_data_path, 'ranking_result')
os.makedirs(result_list_save_path, exist_ok=True)

# retry_list dir path
retry_list_save_path = os.path.join(ranking_data_path, 'retry_list')
os.makedirs(retry_list_save_path, exist_ok=True)

# error_list dir path
error_list_save_path = os.path.join(ranking_data_path, 'error_list')
os.makedirs(error_list_save_path, exist_ok=True)

# search_target dir path
search_target_list_save_path = os.path.join(ranking_data_path, 'search_target')
os.makedirs(search_target_list_save_path, exist_ok=True)

# complete_list dir path
complete_list_save_path = os.path.join(ranking_data_path, 'complete_list')
os.makedirs(complete_list_save_path, exist_ok=True)

# retry_list dir path
retry_case_save_path = os.path.join(ranking_data_path, 'retry_case')
os.makedirs(retry_case_save_path, exist_ok=True)


def file_remove(path):
    try:
        os.remove(path)
    except:
        pass