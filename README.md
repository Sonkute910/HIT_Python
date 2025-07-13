
Python là một ngôn ngữ thông dịch (interpreted language).

Điều này có nghĩa là mã Python không được dịch hoàn toàn thành mã máy trước khi chạy. Thay vào đó, một trình thông dịch (interpreter) sẽ đọc và thực thi từng dòng mã tại thời điểm chạy. Khi bạn chạy một chương trình Python, trình thông dịch sẽ:

Phân tích cú pháp (Parse): Trình thông dịch kiểm tra mã Python để đảm bảo nó tuân thủ các quy tắc ngữ pháp của ngôn ngữ.

Biên dịch thành bytecode (Compile to bytecode): Mã Python sau đó được chuyển đổi thành một dạng trung gian gọi là bytecode (mã byte). Bytecode này không phải là mã máy cụ thể cho bất kỳ nền tảng nào, mà là một dạng mã tối ưu hơn cho việc thực thi. Các tệp bytecode thường có phần mở rộng .pyc.

Thực thi (Execute): Cuối cùng, một máy ảo Python (Python Virtual Machine - PVM) sẽ thực thi bytecode này. PVM là một phần của trình thông dịch, chịu trách nhiệm chuyển đổi bytecode thành các lệnh cấp thấp mà máy tính có thể hiểu và thực thi.

Tại sao Python được thiết kế như vậy?

Tính đa nền tảng (Portability): Vì mã Python được chuyển đổi thành bytecode và chạy trên PVM, nó có thể chạy trên bất kỳ hệ điều hành nào có cài đặt trình thông dịch Python. Bạn viết mã một lần và có thể chạy ở mọi nơi mà không cần biên dịch lại cho từng nền tảng cụ thể.

Phát triển nhanh (Rapid Development): Quá trình thông dịch giúp rút ngắn chu trình phát triển. Bạn có thể chạy và kiểm tra mã ngay lập tức sau khi viết, không cần chờ đợi quá trình biên dịch mất thời gian như các ngôn ngữ biên dịch truyền thống (ví dụ: C++).

Dễ gỡ lỗi (Easier Debugging): Khi có lỗi, trình thông dịch thường chỉ ra dòng mã cụ thể gây ra lỗi, giúp việc gỡ lỗi dễ dàng hơn.

Mặc dù có một bước "biên dịch" trung gian sang bytecode, Python vẫn được coi là ngôn ngữ thông dịch vì quá trình biên dịch này không tạo ra mã máy độc lập có thể chạy mà không cần trình thông dịch, và quá trình thực thi chính vẫn diễn ra từng bước bởi PVM.

Kiến thức buổi 2: Các khái niệm cơ bản trong Python
Dưới đây là tổng quan về các kiến thức quan trọng bạn sẽ tìm hiểu trong buổi 2:

1. Các kiểu dữ liệu trong Python
Kiểu dữ liệu xác định loại giá trị mà một biến có thể lưu trữ và các thao tác có thể thực hiện trên giá trị đó. Python có nhiều kiểu dữ liệu tích hợp sẵn:

Số (Numbers):

Số nguyên (Integers - int): Các số nguyên dương, âm và 0 (ví dụ: 5, -10, 0).

Số thực (Floating-point numbers - float): Các số có phần thập phân (ví dụ: 3.14, -0.5, 2.0).

Số phức (Complex numbers - complex): Các số có dạng a+bj, với a và b là số thực, j là đơn vị ảo (ví dụ: 1 + 2j).

Chuỗi (Strings - str): Tập hợp các ký tự được đặt trong dấu nháy đơn ('...') hoặc dấu nháy kép ("...") (ví dụ: 'Hello', "Python"). Chuỗi là bất biến (immutable), nghĩa là bạn không thể thay đổi từng ký tự trong chuỗi sau khi nó được tạo.

Danh sách (Lists - list): Tập hợp có thứ tự và có thể thay đổi (mutable) các phần tử. Các phần tử có thể có các kiểu dữ liệu khác nhau (ví dụ: [1, 'apple', 3.14]).

Bộ (Tuples - tuple): Tương tự như danh sách nhưng là bất biến (immutable). Một khi đã tạo, bạn không thể thay đổi các phần tử của nó (ví dụ: (1, 'banana', 2.71)).

Tập hợp (Sets - set): Tập hợp không có thứ tự và không chứa các phần tử trùng lặp (ví dụ: {1, 2, 3}).

Từ điển (Dictionaries - dict): Tập hợp các cặp khóa-giá trị (key-value pairs) không có thứ tự. Mỗi khóa là duy nhất và được sử dụng để truy cập giá trị tương ứng (ví dụ: {'name': 'Alice', 'age': 30}).

2. Các toán tử trong Python
Toán tử là các ký hiệu đặc biệt thực hiện các phép tính trên một hoặc nhiều toán hạng.

Toán tử số học (Arithmetic Operators): Dùng để thực hiện các phép toán số học cơ bản.

+ (Cộng)

- (Trừ)

* (Nhân)

/ (Chia)

% (Chia lấy dư)

** (Lũy thừa)

// (Chia lấy phần nguyên)

Toán tử so sánh (Comparison Operators): Dùng để so sánh hai giá trị, trả về True hoặc False.

== (Bằng)

!= (Không bằng)

> (Lớn hơn)

< (Nhỏ hơn)

>= (Lớn hơn hoặc bằng)

<= (Nhỏ hơn hoặc bằng)

Toán tử gán (Assignment Operators): Dùng để gán giá trị cho biến.

= (Gán)

+=, -=, *=, /=, etc. (Gán kết hợp với phép toán)

Toán tử logic (Logical Operators): Dùng để kết hợp các biểu thức điều kiện.

and (Và logic)

or (Hoặc logic)

not (Phủ định logic)

Toán tử nhận dạng (Identity Operators): Kiểm tra xem hai biến có tham chiếu đến cùng một đối tượng trong bộ nhớ hay không.

is

is not

Toán tử thành viên (Membership Operators): Kiểm tra xem một giá trị có tồn tại trong một chuỗi, danh sách, tuple, set hoặc dictionary hay không.

in

not in

3. Mệnh đề điều kiện và Vòng lặp
Đây là các cấu trúc điều khiển luồng chương trình, cho phép bạn thực thi các khối mã khác nhau dựa trên các điều kiện hoặc lặp lại một khối mã nhiều lần.

Mệnh đề điều kiện (if, elif, else):

if: Thực thi một khối mã nếu điều kiện là True.

elif (else if): Thực thi một khối mã khác nếu điều kiện if trước đó là False và điều kiện elif này là True. Bạn có thể có nhiều elif.

else: Thực thi một khối mã nếu tất cả các điều kiện if và elif trước đó đều là False.