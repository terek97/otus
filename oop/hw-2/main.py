from media_files.audio_file import AudioFile
from media_files.video_file import VideoFile
from cloud_storages.yandex_cloud_storage import YandexCloudStorage

# Создание экземпляров медиапрограмм

# Создание аудиофайла
audio_file = AudioFile(path='/music/', name='song.mp3', artist='Artist Name', album='Album Name')
print(f'Audio File: {audio_file.name}')
print(f'Path: {audio_file.path}')
print(f'Artist: {audio_file.artist}')
print(f'Album: {audio_file.album}')
print(f'Creation Date: {audio_file.creation_date}\n')

# Переименование аудиофайла
audio_file.rename_file('new_song.mp3')
print(f'Renamed Audio File: {audio_file.name}\n')

# Создание видео файла
video_file = VideoFile(path='/videos/', name='movie.mp4', resolution='1920x1080')
print(f'Video File: {video_file.name}')
print(f'Path: {video_file.path}')
print(f'Resolution: {video_file.resolution}')
print(f'Creation Date: {video_file.creation_date}\n')

# Извлечение кадров из видео
video_file.extract_frames()
print(f'Frames extracted from {video_file.name}\n')

# Создание облачного хранилища
yandex_cloud = YandexCloudStorage(account='user@example.com')

# Соединение с облачной учетной записью
yandex_cloud.connect(password='your_password')

# Загрузка аудиофайла в облачное хранилище
yandex_cloud.upload(audio_file)
print(f'Uploaded {audio_file.name} to {yandex_cloud.service_name}.\n')

# Загрузка видео файла в облачное хранилище
yandex_cloud.upload(video_file)
print(f'Uploaded {video_file.name} to {yandex_cloud.service_name}.\n')

# Возможность загрузки из облачного хранилища
yandex_cloud.download(audio_file, '/local_path/song.mp3')
print(f'Downloaded {audio_file.name} from {yandex_cloud.service_name} to local path.\n')

# Удаление файла из облачного хранилища
yandex_cloud.delete(audio_file)
print(f'Deleted {audio_file.name} from {yandex_cloud.service_name}.')
