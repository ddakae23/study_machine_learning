import cv2
import pytesseract
def extract_license_plate(image_path, lang='eng+Hangul'):
    # 이미지 읽기
    img = cv2.imread(image_path)

    # 이미지를 그레이스케일로 변환
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 이미지를 가우시안 블러로 흐림 처리
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # 가우시안 블러로 처리된 이미지를 이진화하여 이진 이미지 생성
    binary_image = cv2.adaptiveThreshold(
        img_blur,
        maxValue=255.0,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY_INV,
        blockSize=19,
        C=9
    )

    # 이진 이미지에서 외곽선 찾기
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 외곽선의 길이에 대한 오차를 설정하여 근사 다각형으로 변환
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        # 근사 다각형은 외곽선을 단순화한 다각형 형태로 표현됨

        # 찾은 외곽선이 사각형인 경우
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(contour)

            # 일정 크기의 사각형 영역을 번호판으로 간주
            if 100000 < cv2.contourArea(contour) < 150000:
                # 번호판 영역 추출
                license_plate_roi = img[y:y + h, x:x + w]

                # OCR을 이용하여 번호판 텍스트 추출
                text = pytesseract.image_to_string(license_plate_roi, lang=lang, config='--psm 8')

                # 추출된 텍스트 출력
                print(f"Text in License Plate: {text}")

                # 번호판 영역에 사각형 그리기
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 결과 이미지 출력
    cv2.imshow('License Plate Recognition', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 테스트할 이미지 경로
image_path = '222.jpg'
extract_license_plate(image_path)
