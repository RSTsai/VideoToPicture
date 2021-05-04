import cv2
from os import makedirs, path



# 影片檔名
VideoName = '153749'
# 影片全路徑
VideoPath = f'./VideoToPicture/20210325/videoCam0/{VideoName}.avi' 
# 取樣幀數間隔
FrameDelta = 150 
# 圖像resize尺寸
SizeW = 640
SizeH = 480


# 存檔資料夾
SaveFolder = './VideoToPicture/JPEGImages/'
# 存檔名稱開頭
SaveFileNameHeader = f'NN_{VideoName}_'
# 存檔名稱起始編號
SaveNumStart = 0
# 存檔名稱數字位數 (zfill)
ZfillNum = 6 



def GetImagesFromVideo(VideoPath, deltaF):
    frameNum = 0
    saveNum = 0
    video_images = []

    # 確認存檔資料夾存在
    if CheckDir(SaveFolder) == False:
        return

    # 判斷是否開啟影片
    vc = cv2.VideoCapture(VideoPath) 
    if vc.isOpened():
        rval = True
    else:
        rval = False

    # 擷取視頻至結束
    while rval:   
        rval, video_frame = vc.read()

        # 每一幀+1
        frameNum = frameNum + 1   

        # 讀取不到影像則跳過
        if rval == False:
            continue
        
        # 每隔幾幀進行擷取
        if(frameNum % deltaF == 0): 
            # 每保存一張saveNum+1
            saveNum = saveNum + 1 
            # 存檔檔名
            saveFileName = SaveFolder + SaveFileNameHeader + str(SaveNumStart + saveNum).zfill(ZfillNum)+ '.jpg'
            # 圖像格式化
            video_frame_format = cv2.resize(video_frame, (SizeW,SizeH))
            # 保存圖像
            saveImage(video_frame_format, saveFileName)
            video_images.append(video_frame_format)   
            # 顯示圖像
            # cv2.imshow('windows', video_images[i])
            # cv2.waitKey(100)

    vc.release()
    cv2.destroyAllWindows
    return video_images


def saveImage(image,saveFilePath):
    print('save image: ',saveFilePath)
    cv2.imwrite(saveFilePath,image)

 
def CheckDir(dirPath):
    try:
        if path.exists(dirPath):
            return True
        else:
            print("路徑不存在。")
            print(f"建立路徑:{dirPath}")
            makedirs(dirPath)
            return True
    except FileExistsError:
        print("路徑已存在")
        return True
    except PermissionError:
        # 權限不足的例外處理
        print("權限不足")
        return False



if __name__ =="__main__":
    # 讀取影片並轉成圖片
    video_images = GetImagesFromVideo(VideoPath, FrameDelta) 

