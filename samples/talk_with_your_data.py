from rich import print

from geminiplayground import GeminiClient, VideoFile, ImageFile, HarmCategory, HarmBlockThreshold

if __name__ == "__main__":
    gemini_client = GeminiClient()

    video_file_path = "BigBuckBunny_320x180.mp4"
    video_file = VideoFile(video_file_path, gemini_client=gemini_client)
    # video_file.upload()

    image_file_path = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
    image_file = ImageFile(image_file_path, gemini_client=gemini_client)
    # image_file.upload()

    prompt = [
        "See this video",
        video_file,
        "and this image",
        image_file,
        "What do you think?"
    ]

    response = gemini_client.generate_response("models/gemini-1.5-pro-latest", prompt,
                                               generation_config={"temperature": 0.0, "top_p": 1.0},
                                               safety_settings={
                                                   "category": HarmCategory.DANGEROUS_CONTENT,
                                                   "threshold": HarmBlockThreshold.BLOCK_NONE
                                               })
    # Print the response
    for candidate in response.candidates:
        for part in candidate.content.parts:
            if part.text:
                print(part.text)
