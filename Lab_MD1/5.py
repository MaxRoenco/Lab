from PIL import Image, ImageDraw

n = int(input("Enter the size: "))
size = 3 ** n
total_operations = (8 ** n - 1) / 7
done_operations = 0
persentage = 0
print("Progress: 0%")
carpet = Image.new("RGB", (size, size))
draw = ImageDraw.Draw(carpet)
draw.rectangle([0, 0, size, size], fill='black')


def holify(start_x, start_y, end_x, end_y, n):
    global done_operations
    global persentage
    n -= 1
    if n < 0:
        return
    diff = (end_x - start_x) / 3
    hole_start_x = start_x + diff
    hole_start_y = start_y + diff
    hole_end_x = end_x - diff - 1
    hole_end_y = end_y - diff - 1
    draw.rectangle([hole_start_x, hole_start_y, hole_end_x, hole_end_y], fill='white')
    done_operations += 1
    new_persentage = int((done_operations / total_operations) * 100)
    if new_persentage != persentage:
        persentage = new_persentage
        print("Progress: " + str(persentage) + "%")

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            recursive_start_x = start_x + diff * i
            recursive_start_y = start_y + diff * j
            recursive_end_x = recursive_start_x + diff
            recursive_end_y = recursive_start_y + diff
            holify(recursive_start_x, recursive_start_y, recursive_end_x, recursive_end_y, n)


holify(0, 0, size, size, n)
carpet.save("carpet.png")
carpet.show()
