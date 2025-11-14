import asyncio
from yt_dlp import YoutubeDL

async def download_video(url: str, output_path: str):
    ydl_opts = {
        "outtmpl": f'{output_path}/%(title)s.%(ext)s',
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }
    
    def _run_dl():
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # Обработка плейлиста
            if "entries" in info:
                info = info["entries"][0]

            filename = ydl.prepare_filename(info)

            video_fmt = None

            if "requested_formats" in info:
                for f in info["requested_formats"]:
                    if f.get("vcodec") != "none":
                        video_fmt = f
                        break
            else:
                video_fmt = info

            format_note = None

            if video_fmt:
                format_note = video_fmt.get("format_note")

            return {
                "filename": filename,
                "format_note": format_note,
            }
        
    return await asyncio.to_thread(_run_dl)