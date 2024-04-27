from hfutils.index import hf_tar_file_download

def divide_and_pad(id, dividend, padded_count):
    result = id // dividend
    result_length = len(str(result))
    if result_length > padded_count:
        raise ValueError("Division result exceeds padded count")
    padded_result = str(result).zfill(padded_count)
    return padded_result

class 
repo_owner = 'shiertier'
repo_name = '12TPIC'
repo_id = repo_owner + '/' + repo_name
repo_type = 'dataset'
image_host = 'danbooru'
# image_host_list = ['danbooru', 'pixiv', 'artstation', 'z', 'relu34', 'gelbooru', 'relu34', 'pin']
dan_image_size = {
    0: 'origin', 
    512: 'webp_512',
    1024: 'webp_1024', 
    2048: 'webp_2048'
    }
image_size = 1024
size_path = dan_image[image_size]
m_path = divide_and_pad(id, 1000000, 2)
tar_file = divide_and_pad(id, 10000, 4) + '.tar'
archive_in_repo = os.path.join(image_host, size_path, m_path, tar_file)
file_in_archive = str(id) + ext

hf_tar_file_download(
    repo_id='shiertier/12TPICS',
    repo_type='dataset',
    archive_in_repo=f'danbooru/0{id_ % 1000:03d}.tar',
    file_in_archive=filename,
    local_file=dst_file,
    )
