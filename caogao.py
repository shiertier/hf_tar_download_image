from hfutils.index import hf_tar_file_download
import os.path

def divide_and_pad(id, dividend, padded_count):
    result = id // dividend
    result_length = len(str(result))
    if result_length > padded_count:
        raise ValueError("Division result exceeds padded count")
    padded_result = str(result).zfill(padded_count)
    return padded_result

class hf_pic_download:
	def __int__(self,
						save_directory: str,
						image_size: int = 1024,
						image_host: str = 'danbooru',
						):
		self.repo_owner = 'shiertier'
		self.repo_name = '12TPIC'
		self.repo_id = repo_owner + '/' + repo_name
		self.repo_type = 'dataset'
		image_host_list = ['danbooru', 'pixiv', 'artstation', 'z', 'relu34', 'gelbooru', 'relu34', 'pin']
		if image_host in image_host_list:
			self.image_host = image_host
		else:
			rasie KeyError'not have this host'
		self.image_size = image_size
		self.save_path = save_path
			
	def _dan_format_path(self, 
								id: int,
								ext: str = 'webp'):
		dan_image_size = {
   		 0: 'origin', 
    		512: 'webp_512',
    		1024: 'webp_1024', 
    		2048: 'webp_2048'
    		}
    	try:
    		size_path = dan_image[image_size]
		except Keyerror:
			raise
		m_path = divide_and_pad(id, 1000000, 2)
		tar_file = divide_and_pad(id, 10000, 4) + '.tar'
		archive_path = os.path.join(image_host, size_path, m_path, tar_file)
		file_in_archive = str(id) + ext
	return archive_path, file_in_archive

	def download_dan_pic(self, 
											 id: int,
											 ext: str = 'webp'):
		local_pic_path = os.path.join(self.save_path, str(id) + ext)
		repo_archive_path, repo_image_name = self._dan_format_path(id, ext)
		hf_tar_file_download(
    		repo_id=self.repo_id,
    		repo_type=self.repo_type,
    		archive_in_repo=repo_archive_path,
    		file_in_archive=repo_image_name,
    		local_file=local_pic_path,
    		)
