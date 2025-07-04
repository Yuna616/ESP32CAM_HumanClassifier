# server/result_storage.py

import os, json, shutil

class ResultStorage:
    def __init__(self, image_dir, save_path):
        self.image_dir = image_dir
        self.save_path = save_path

        os.makedirs(self.image_dir, exist_ok=True)

    def save(self, image_file, image_filename, label, confidence, timestamp):
        image_path = os.path.join(self.image_dir, image_filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image_file, buffer)

        try:
            with open(self.save_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        data.append({
            "image_name": image_filename,
            "label": label,
            "confidence": confidence,
            "timestamp": timestamp
        })

        with open(self.save_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_by_timestamp(self, timestamp):
        try:
            with open(self.save_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return False

        new_data = []
        deleted_image = None
        for entry in data:
            if entry.get("timestamp") == timestamp:
                deleted_image = entry.get("image_name")
            else:
                new_data.append(entry)

        if deleted_image:
            image_path = os.path.join(self.image_dir, deleted_image)
            if os.path.exists(image_path):
                os.remove(image_path)

        with open(self.save_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)

        return bool(deleted_image)

    def load_results(self):
        try:
            with open(self.save_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
