import m3u8
import requests
url="Enter the url to the m3u8 file here"
r=requests.get(url)
m3u8_index=m3u8.loads(r.text)
print(m3u8_index.data)
playlist_url=m3u8_index.data['playlists'][3]['uri']
r=requests.get(playlist_url)
playlist=m3u8.loads(r.text)
print(playlist.data['segments'][0]['uri'])
r=requests.get(playlist.data['segments'][0]['uri'])
with open('video.ts','wb') as f:
    for segment in playlist.data['segments']:
        url=segment['uri']
        r=requests.get(url)
        f.write(r.content)
import subprocess
subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])
CompletedProcess(args=['ffmpeg', '-i', 'video.ts', 'video.mp4' ], returncode=0)







