import cv2
import os
from vidgear.gears import CamGear
import shutil
import time

data = ['tnTPaLOaHz8', 'Wdjh81uH6FU', '7dYTw-jAYkY', 'mwKJfNYwvm8', 'QjvpjXdgugA', '3ryID_SwU5E', '3OFj6l2tQ9s', 'KrLj6nc516A', 'vBpQ1SlfVtU', 'J_z-W4UVHkw', 'jObOjhUkf50', 'yhB3BgJyGl8', 'fuhE6PYnRMc', '48h57PspBec', 'FM7Z-Xq8Drc', 'WTOm65IZneg', 'YLt73w6criQ', 'TJ2ifmkGGus', '7IKab3HcfFk', 'h5NvTTOlOtI', '0CTp1a-aCUM', 'kX3nB4PpJko', 'iogcY_4xGjo', 'gHzuabZUd6c', '65fN_OUawjk', 'jdMNoQE3mIQ', '2isYuQZMbdU', 'tVWWp1PqDus', 'vaIgyRoUkQI', 'Hwybp38GnZw', 'hD1YtmKXNb4', 'LnlKwzc_TNA', '3jS_yEK8qVI', '00NgUctWoLQ', 'x9TQ6culXIA', 'QbJJwaVdgIs', '0e3GPea1Tyg', 'cV2gBU6hKfY', 'qIsgdOVGA04', 'cExLQ1o2pDw', 'uocETPj4Jx4', 'hxwpkM5w3Cc', 'ktyJIj6i4Qw', 'urtFrxDUV6c', 'nM89Wl03Q4g', 'NZlClr_ivb4', 'E6E22XQPhhg', 'TQHEJj68Jew', 'WcwGleN38zE', 'fMfipiV_17o', 'ayXxwJJId_c', '9bqk6ZUsKyA', 'DuQbOQwVaNE', 'vJH28ICkCdU', '_uwNDiU04zE', 'C680oxL__ck', '5Fg9oZk-5uA', 'PKtnafFtfEo', 'f0c7pSCoZqE', 'dg2Ag3e8W-Q', 'LeYsRMZFUq0', 'Dc2ZRmuH5OM', 'GLoeAJUcz38', 'SZQhgExjBvQ', 'IoZri9hq7z4', 'vp5sSqyZ5Go', 'AKJfakEsgy0', 'Vl3swga-Xrk', 'UE5AHE2Ypr8', 'TDiXxsQ0w2Q', 'oD155zWANQg', 's1ax8Tx_Jz0', 'FbM1yi4mMMc', '5V2B28OqfqM', 'Rj_vssRaZlQ', 'YQDDm9HLkV4', 'erQ_9yEz0ls', 'OAbP-V6fEVc', '_qAJMXfL6o0', '59AYXzCa-Cs', 'r7zJ8srwwjk', 'YSoJPA8-oHc', '5Hg_QSIJm8I', 'HBMmK1c44sE', 'oBYbxw8f5OI', '_mdKvblL_8s', 'yXWw0_UfSFg', 'KSKJKLmAqpI', 'IYVjOfoU3uI', 'oI6aXhowFDY', 'LdMx2U5tby0', 'fY-LA3YaZ_M', '0hVZOJCYBBM', 'Z9WQy9jEY8M', 'bs0SWXbty18', 'yeqARWqjkps', 'wMuYiLby3-s', 'NbaWrbJDr48', 'sfv1QaRzJg8', 'RwnN2FVaHmw', 'X1jMMFOqxEw', 'ORUX1lHbOa8', 'LU_xVr4b2qM', 'tQ4m4zD7BBA', 'D9lVNzyhYnc', 'jokVbbLqV_E', 'HPJKxAhLw5I', 'Ims5p6wjW9s', 'anFxsa5jXrE', 'QxGVgXf_LNk', 'al6130OD1Ck', 'd1010B3sKNQ', 'NS3hse9ezik', 'npDey6_9YRs', '0NGWT9COcEI', 'bTrV5v7GLcQ', 'lBYC4_Lccjw', 'gL6iSCSHjco', 'UQtltNZ_pjs', '0DaMUhgcAqo', 'TOcGSwJBPMQ', 'ws694xrKopA', 'UtnsWzaoRtg', '6wsFjjhZPJI', 'Rmf6T_Ewt38', 'n6qc4LHN2KQ', '2eFSU7TFOnk', 'RCvnytndd9c', 'AA-VpIj8F5Y', 'fWcSBWadolA', 'YyhKdOCwD7s', 'ha4tRQwKIUg', 'xRwy_rKc7gI', 'H1WBdh56Vq4', 'xhIYirjB4Yc', 'HfJMs4mrSJM', 'tYHTVjfShOA', 'JTQcIR2ZxU4', 'xpNeg0hPZIs', '9yrdFAJUSaU', 'i2O6GMpNWGo', 'Y6jC6VaO3j0', 'Ooke4YZv8Ts', 'ZV7rU6lnAKQ', 'iUzi5JmJNWc', '9cCpZl8euLI', 'I046_n20d3s', '2nd73lyvq4w', 'nuM0Z4a7kMs', 'qPBtTPJHS0Q', 'A-vX1AGBGsc', 'IiW2smvEcBM', 'q6Qw8mUVTrE', 'dBxOYE2j55U', '984NGLLYDUg', '7zi0bi-RDj4', 'XaxhLbxZ13k', 'L8nh1wuXTbI', '9-HphHIJS9c', 'rPXmbM2UEbU', 'sESRuTyfsEk', 'QapO3maXd9k', '71VpdDb8e6U', 'Su34c5Z8DW4', 'e5DqdX-7_g4', '9vB-48kHbBU', '3ix_gbcubTo', 'VqnQ-0q2gb4', '3TflpIllQHY', '1SwVSTKFCsc', 'ZPuEUe_8SRM', 'gKVZz4kcuns', 'nywT2SenPIo', 'xBP9EUQIkNs', 'qZNxvnQv0h4', 'uE6gud1voDs', 'f0M64XpmTz8', 'Gz3yak1cl-8', '9GD6hbqu2oM', 'GUWGsIVEMSQ', 'wDqJZ_2ZA3A', 'RywkkwO78m8', 'P4qWhSZ7_WA', 'UlUcwJc5nBs', 'qAW6CE7_bFM', 'tBEBc4KQVsU', 'q0OK-zHnvnA', 'bFZdU9dr4OM', 'nd-bwvNB7YA', '6_im_hGxGRk', 'b91vrgVY-ZQ', '52ubXjlVzUY', 'XHb7g6yuGgE', 'rH1D_3G56DY', '-0zoWMSEOGg', 'WRzIuC2MKOU', '3iaDrpKdaIc', 'qrIh-ZHN4-E', 'mpZWt5pGKZ8', 'vbph9F_pRNI', 'XE9pUM9MEFA', 'wbzD04leeLI', 'MC5h-ShR-S8', 'dp8IaLrZpGs', '97Gh93Daio0', 't4OumncEiKo', 'Ejou8aa5eZk', 'ehEuczQUh8E', 'uBC7805Smsg', 'd8pJkuSp1iI', 'dFr5YQaQQdo', 'xBLxMfO3pDw', 'yuGEB4ZZdUQ', 'yOAUGrSG3Po', 'Sj0ryLzaP1M', 'fz0fl0TJgIM', 'F8y8Y16lF-Y', 'R06LnZoLeng', 'b2RV4_cbOH8', 'RBi9OPAVQdc', '1XbDoj1aOrM', 'SvA00veV-Vs', 'kezT2QZ4Ypc', '_MJmgIApH64', 'p9rYqicga20', 'RgDSdoHLNPo', 'YkIN3TyDLFk', '_7VXXHn-AaY', 'nY0PhNhogYw', 'dUaTLrPXQCE', 'CFYwwwuZzj0', 'hUmTKH68EVE', 'JMiZw-tzYLo', '8wdUkGIaCwY', '76qnNkZ6-bA', 'PK6G7wr-SA0', 'meqTnHzXZus', 'cVU7iUq_XmA', 'vgd20co9vp8', 'UTH-B5E46O0', 'OW2eTF2CKo0', 'CEuQR5hoBJs', 'A3F9BTLSZEA', 'Lf6QMsdSn_4', 'oQwd7ygDAD4', 'RPH2APBoVtI', 'CUQH-sZQoDk', 'S9EnUSSU7HI', 'LrTKeT8xBRg', '3Z96uuV_bkI', '6kKHApOP9GA', 'n5Op1CIdg4Y', 'f7078psRdIY', 'MR7zZ7XEl6M', 'mPTKyGKUevo', 'PJqlSJ8pzy8', 'lg2cdA2BglE', 'Elf049m0V7k', 'U1bUwDxBu4Y', 'AWbo7tblwwE', 'b6fIzFW6M1w', '-K2riQhCyF4', 'xcGiyOxZpCw', 'xBDvhnuYMbc', 'JCgk-mnngY4', 'p2nubPAIGcA', 'K6LiS5qTmHo', 'p6QAMEdB_BM', 'w3rHYUlj5gQ', '65nfbW-27ps', 'I3TzYJqVsxM', 'gvgkVpm4KVw', 'iWWWyG5ZwG8', '7__r4FVj-EI', 'JdFRjsEZrmU', 'Zb01RStdzEs', '9c2NqlUWZfo', 'md75n8cyenA', '1UTjWy-vnOo', 'T9xsTO6ujqM', 'DOWDNBu9DkU', '2JAOTJxYqh8', 'iWeu2dxHRDg', 'lg5wznn3IBE', 'Rsxao9ptdmI', 'h8g9wfI9nGI', 'xsLJZyih3Ac', 'uBEL3YVzMwk', 'QiKZYt9070U', '3c584TGG7jQ', 'e09xig209cQ', '8HEfIJlcFbs', 'VS6tnF31zr4', 'DTvS9lvRxZ8', 'VrKW58MS12g', 'h4T_LlK1VE4', 'vePc5V4h_kg', 'hFZFjoX2cGg', 'I5-dI74zxPg', 'tMKXbLBgkEc', '-k-V3ESHcfA', 'a_TSR_v07m0', 'wM5NHC97JBw', 'Kou7ur5xt_4', 'ugRc5jx80yg', 'PmlRbfSavbI', 'oBcxuzdP3rs', '6qZWMNW7GmE', 'xoxhDk-hwuo', 'pFEB0chiuJA', 'GYCI58pMGuQ', 'LEZCxxKp0hM', 'zwgaTYOx0RI', 'M0_U1FHwACk', 'b7zWwo9dbiU', 'vXBfwgwT1nQ', 'My4RA5I0FKs', 'S32y9aYEzzo', 'T1KRQ3RcvXA', 'lv8wqnk_TsA', 'vNds3PIBqnQ', 'MHTizZ_XcUM', 'Qf-D1Upn-KU', '350Xlkvn0Ko', 'v4c0IBeXwY8', '_uXnypEzau0', 'I6IqoSAtjb0', 'GMb6GNYPqXA', 'MFVXsnq230c', '57MKxz4pJKE', 'W4DnuQOtA8E', 'pR5VJo5ifdE', 'JinpVA6p8Mo', 'FRlbNOno5VA', 'nsnyl8llfH4', '8Vc-69M-UWk', '-RjJtO51ykY']

# Base path where you want to save the folders and images
path = "videos/"
data = data[291:]
# # Iterate through each video ID
# for video_id in data:
#     video_url = f"https://www.youtube.com/watch?v={video_id}"
#     stream = CamGear(source=video_url, stream_mode=True, logging=True).start()

#     # Create a directory for the current video ID
#     os.makedirs(os.path.join(path, video_id), exist_ok=True)

#     frame_counter = 0  # Counts every frame
#     save_interval = 150  # Save a frame every 150 frames (5 seconds)

#     while True:
#         frame = stream.read()
#         if frame is None:
#             break

#         # Save a frame every 5 seconds
#         if frame_counter % save_interval == 0:
#             frame_name = os.path.join(path, video_id, f"{video_id}_{frame_counter // save_interval}.jpg")
#             print(f"Saving {frame_name}")
#             cv2.imwrite(frame_name, frame)

#         frame_counter += 1

#     stream.stop()

# cv2.destroyAllWindows()


def delete_folder_if_exists(folder_path):
    """Deletes the folder if it exists."""
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Delete all files and folders contained in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        # Delete the folder itself
        os.rmdir(folder_path)
        print(f"Deleted folder: {folder_path}")

for video_id in data:
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    attempts = 0
    max_attempts = 5
    success = False

    while not success and attempts < max_attempts:
        try:
            stream = CamGear(source=video_url, stream_mode=True, logging=True).start()
            fps = round(stream.framerate)
            save_interval = round(fps * 5)  # Save a frame every 5 seconds
            print("The fps is: ", str(fps))
            success = True  # If the stream is successfully initialized
        except RuntimeError as e:
            print(f"Failed to initialize stream for {video_id}: {str(e)}")
            attempts += 1
            time.sleep(5)  # Wait for 5 seconds before retrying

    if success:
        if fps != 30:
            folder_path = os.path.join(path, video_id)
            delete_folder_if_exists(folder_path)
            os.makedirs(folder_path, exist_ok=True)

            frame_counter = 0

            while True:
                frame = stream.read()
                if frame is None:
                    break

                if frame_counter % save_interval == 0:
                    frame_name = os.path.join(folder_path, f"{video_id}_{frame_counter // save_interval}.jpg")
                    print(f"Saving {frame_name}")
                    cv2.imwrite(frame_name, frame)

                frame_counter += 1

            stream.stop()

cv2.destroyAllWindows()