import re

# Hàm chuẩn hóa tên tài khoản TikTok
def chuan_hoa_tai_khoan(username):
    username = username.strip()  # loại bỏ khoảng trắng đầu/cuối
    if not username:  # kiểm tra rỗng
        return None, "Tên tài khoản không được rỗng"
    return f"@{username.lower()}", None  # thêm @ và chuyển thành chữ thường

# Hàm thống kê dữ liệu video
def thong_ke_video(username, title, description, hashtags):
    username = username.strip()
    if not username:
        print("Tên tài khoản không được rỗng")
        return
    description = description.strip()
    if not description:
        print("Mô tả video không được rỗng")
        return

    # Chuẩn hóa tiêu đề: bỏ khoảng trắng, viết hoa chữ cái đầu mỗi từ
    title = title.strip().title()
    # Chuẩn hóa danh sách hashtag: bỏ khoảng trắng thừa
    hashtags = [h.strip() for h in hashtags.split(",") if h.strip()]

    # Xuất báo cáo thống kê
    print("\n--- Báo cáo thống kê ---")
    print("Tên tài khoản:", username)
    print("Tiêu đề:", title)
    print("Mô tả:", description)
    print("Độ dài mô tả:", len(description))
    print("Số lượng từ trong mô tả:", len(description.split()))
    print("Danh sách hashtag:", hashtags)
    print("Số lượng hashtag:", len(hashtags))
    print("Mô tả chữ thường:", description.lower())
    print("Mô tả chữ hoa:", description.upper())

# Hàm kiểm tra hashtag hợp lệ
def kiem_tra_hashtag(hashtag):
    if not hashtag:
        return "Hashtag không được rỗng"
    if not hashtag.startswith("#"):
        return "Hashtag phải bắt đầu bằng ký tự #"
    if " " in hashtag:
        return "Hashtag không được chứa khoảng trắng"
    if len(hashtag) < 2:
        return "Hashtag phải có ít nhất 2 ký tự"
    # Regex kiểm tra ký tự hợp lệ sau dấu #
    if not re.match(r"^#[A-Za-z0-9_]+$", hashtag):
        return "Hashtag chỉ nên dùng chữ cái, chữ số hoặc dấu gạch dưới"
    return "Hashtag hợp lệ"

# Hàm tìm kiếm và thay thế từ khóa trong mô tả
def tim_kiem_thay_the(description, keyword, replacement):
    count = description.count(keyword)  # đếm số lần xuất hiện
    if count == 0:
        print("Không tìm thấy từ khóa cần tìm trong mô tả.")
    else:
        new_desc = description.replace(keyword, replacement)  # thay thế
        print("Mô tả sau khi thay thế:", new_desc)
        print("Số lần xuất hiện từ khóa:", count)

# Menu chính của chương trình
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Nhập dữ liệu và xem báo cáo thống kê")
        print("2. Chuẩn hóa tên tài khoản TikTok")
        print("3. Kiểm tra hashtag hợp lệ")
        print("4. Tìm kiếm và thay thế từ khóa trong mô tả video")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ")
        if not choice.isdigit():  # kiểm tra nhập không phải số
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5.")
            continue

        choice = int(choice)
        if choice == 1:
            username = input("Nhập tên tài khoản: ")
            title = input("Nhập tiêu đề video: ")
            description = input("Nhập mô tả video: ")
            hashtags = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
            thong_ke_video(username, title, description, hashtags)

        elif choice == 2:
            username = input("Nhập tên tài khoản: ")
            chuan_hoa, error = chuan_hoa_tai_khoan(username)
            if error:
                print(error)
            else:
                print("Tên tài khoản ban đầu:", username)
                print("Tên tài khoản chuẩn hóa:", chuan_hoa)

        elif choice == 3:
            hashtag = input("Nhập hashtag: ")
            result = kiem_tra_hashtag(hashtag)
            print(result)

        elif choice == 4:
            description = input("Nhập mô tả video: ")
            keyword = input("Nhập từ khóa cần tìm: ")
            replacement = input("Nhập từ khóa thay thế: ")
            tim_kiem_thay_the(description, keyword, replacement)

        elif choice == 5:
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    menu()
