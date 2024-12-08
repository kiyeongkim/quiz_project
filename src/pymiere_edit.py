import os
import time
import pymiere
from pymiere.wrappers import time_from_seconds

# Python 파일의 현재 디렉토리 경로 가져오기
current_directory = os.path.dirname(os.path.abspath(__file__))

# assets 폴더 경로
asset_path = os.path.abspath(os.path.join(current_directory, "..", "assets"))

# project 파일 경로
project_path = os.path.join(asset_path, "project", "quiz.prproj")

# Premiere Pro에서 프로젝트 파일 실행 후 잠시 대기
os.startfile(project_path)
time.sleep(15)

# Pymiere를 통해 프로젝트에 연결
app = pymiere.objects.app

# 시퀀스 목록 출력
sequences = app.project.sequences
for i, seq in enumerate(sequences):
    print(f"Sequence {i}: {seq.name}")

# 특정 시퀀스를 선택
selected_sequence = sequences[1]

# 선택한 시퀀스를 활성화
app.project.activeSequence = selected_sequence

# Premiere Pro 종료
app.quit()

print("프리미어 작업 종료")
