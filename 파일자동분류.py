import os
import shutil
import re

def classify_files(source_folder, target_folders):
    """
    주어진 폴더에서 파일을 분류하는 함수

    Parameters:
    - source_folder (str): 파일을 읽어올 폴더 경로
    - target_folders (dict): 분류된 파일을 이동시킬 대상 폴더들의 경로

    Returns:
    - None
    """

    # 대상 폴더들이 없다면 생성
    for folder in target_folders.values():
        if not os.path.exists(folder):
            os.makedirs(folder)

    # 소스 폴더 내의 파일 목록 조회
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # 파일인지 확인
        if os.path.isfile(file_path):
            # 파일의 확장자를 가져옴
            _, file_extension = os.path.splitext(filename)
            
            # 이미지 파일 체크 (jpg, jpeg, png, gif 확장자)
            if re.search(r'\.(jpg|jpeg|png|gif)$', file_extension, re.IGNORECASE):
                target_folder = target_folders['images']
            # PDF 파일 체크
            elif file_extension.lower() == '.pdf':
                target_folder = target_folders['pdfs']
            # Excel, CSV, 텍스트 파일 체크
            elif file_extension.lower() in ['.xlsx', '.csv', '.txt']:
                target_folder = target_folders['datas']
            else:
                # 위 조건에 해당하지 않는 파일은 분류하지 않음
                continue

            # 대상 폴더로 파일 이동
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"파일 '{filename}'을(를) {target_folder} 폴더로 이동했습니다.")

# 소스 폴더 및 대상 폴더 경로 설정
source_folder = r'C:\Users\student\Downloads'
target_folders = {
    'images': r'C:\Users\student\Downloads\images',
    'pdfs': r'C:\Users\student\Downloads\pdfs',
    'datas': r'C:\Users\student\Downloads\datas',
}

# 파일 분류 함수 호출
classify_files(source_folder, target_folders)