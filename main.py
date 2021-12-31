from  function import dataset
import  cv2
import  numpy as np
from pyzbar.pyzbar import decode

cam=cv2.VideoCapture(0)
barcode_data,barcode_target=dataset()
while True:
    _,frame=cam.read()
    code=decode(frame)
    for barcode in code:
        input_data=barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 0, 255), 5)

        if input_data in barcode_data:
            pts2 = barcode.rect
            cv2.putText(frame, input_data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            print("This product is available")

    if cv2.waitKey(1)==ord('q'):
        break
    cv2.imshow("frame",frame)









