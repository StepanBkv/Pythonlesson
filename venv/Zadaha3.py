class Rectangle(object):
    def __init__(self, ident, val):
        self.__id = ident
        self.__value = val

    def get_value(self):
        return self.__value

    def change_value(self, val):
        self.__value = val
        self.__id = str(val)

    def move(self):
        f = False
        while f == False:
            rect_id = input(
                "Введите 4 точки прямоугольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
            lt = list(map(str, rect_id.split(' ')))
            stri = ''
            try:
                if len(lt) != 4:
                    raise Uncorrect("")
                try:
                    for i in range(len(lt)):
                        lt[i] = lt[i].replace('(', '')
                        lt[i] = lt[i].replace(')', '')
                        lt[i] = lt[i].replace(' ', '')
                        stri += lt[i] + ' '
                    tmp = tuple([(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
                    try:
                        if Rect_is_Exist(tmp) != True:
                            raise Non_existence_of_rectiangle_except("Не существует такого прямоугольника!")
                        f = True
                        self.__value = tmp
                        self.__id = str(tmp)
                    except Non_existence_of_rectiangle_except as exc:
                        print(exc)
                except ValueError:
                    print("Координата может быть только числом!")
            except Uncorrect as excep:
                pass

    def __del__(self):
        pass


class Non_existence_of_triangle_except(Exception):
    pass


class Non_existence_of_rectiangle_except(Exception):
    pass


class Uncorrect(Exception):
    pass


def Triangle_is_Exist(kort):
    x1 = kort[0][0] - kort[2][0]
    y1 = kort[0][1] - kort[2][1]
    x2 = kort[1][0] - kort[2][0]
    y2 = kort[1][1] - kort[2][1]
    if abs(((y1 / x1) - (y2 / x2))) > 0:
        return True
    else:
        return False


def Rect_is_Exist(cort):
    a = math.sqrt((cort[1][0] - cort[0][0]) ** 2 + (cort[1][1] - cort[0][1]) ** 2)
    b = math.sqrt((cort[2][0] - cort[1][0]) ** 2 + (cort[2][1] - cort[2][1]) ** 2)
    c = math.sqrt((cort[3][0] - cort[2][0]) ** 2 + (cort[3][1] - cort[3][1]) ** 2)
    d = math.sqrt((cort[0][0] - cort[3][0]) ** 2 + (cort[0][1] - cort[3][1]) ** 2)
    return True if (a + b + c >= d) and (a + c + d >=b) and (a + b + d >= c) and (b + c + d >= a) else False


class Triangle(object):
    def __init__(self, ident, val):
        self.__id = ident
        self.__value = val

    def get_value(self):
        return self.__value

    def change_value(self, val):
        self.__value = val
        self.__id = str(val)

    def move(self):
        f = False
        while f == False:
            trian_id = input(
                "Введите 3 новые точки треугольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
            lt = list(map(str, trian_id.split(' ')))
            stri = ''
            try:
                if len(lt) != 4:
                    raise Uncorrect("")
                try:
                    for i in range(len(lt)):
                        lt[i] = lt[i].replace('(', '')
                        lt[i] = lt[i].replace(')', '')
                        lt[i] = lt[i].replace(' ', '')
                        stri += lt[i] + ' '
                    tmp = tuple([(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
                    try:
                        if Rect_is_Exist(tmp) != True:
                            raise Non_existence_of_rectiangle_except("Не существует такого прямоугольника!")
                        f = True
                        self.__value = tmp
                        self.__id = str(tmp)
                    except Non_existence_of_rectiangle_except as exc:
                        print(exc)
                except ValueError:
                    print("Координата может быть только числом!")
            except Uncorrect as excep:
                pass

    def __del__(self):
        pass


def isIntersect(rect, trian):
    fl = 0
    if len(rect.get_value()) == 0 or len(trian.get_value()) == 0:
        print("Заполните координаты фигур!")
        if len(rect.get_value()) == 0:
            while f == False:
                rect_id = input(
                    "Введите 4 точки четырёхгольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
                lt = list(map(str, rect_id.split(' ')))
                stri = ''
                try:
                    if len(lt) != 4:
                        raise Uncorrect("")
                    try:
                        for i in range(len(lt)):
                            lt[i] = lt[i].replace('(', '')
                            lt[i] = lt[i].replace(')', '')
                            lt[i] = lt[i].replace(' ', '')
                            stri += lt[i] + ' '
                        tmp = tuple([(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
                        try:
                            if Rect_is_Exist(tmp) != True:
                                raise Non_existence_of_rectiangle_except("Не существует такого прямоугольника!")
                            f = True
                            rect.change_value(tmp)
                        except Non_existence_of_rectiangle_except as exc:
                            print(exc)
                    except ValueError:
                        print("Координата может быть только числом!")
                except Uncorrect as excep:
                    pass
        if len(trian.get_value()) == 0:
            while f == False:
                trian_id = input("Введите 3 точки треугольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
                lt = list(map(str, trian_id.split(' ')))
                stri = ''
                try:
                    if len(lt) != 3:
                        raise Uncorrect("")
                    try:
                        for i in range(len(lt)):
                            lt[i] = lt[i].replace('(', '')
                            lt[i] = lt[i].replace(')', '')
                            lt[i] = lt[i].replace(' ', '')
                            stri += lt[i] + ' '
                        tmpi = tuple(
                            [(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
                        try:
                            if Triangle_is_Exist(tmp) != True:
                                raise Non_existence_of_triangle_except("Не существует такого треугольника!")
                            f = True
                            trian.change_value(tmpi)
                        except Non_existence_of_rectiangle_except as exc:
                            print(exc)
                    except ValueError:
                        print("Координата может быть только числом!")
                except Uncorrect as excep:
                    pass
    f = False
    for trian_ind in range(len(trian.get_value()) - 1):
        for rect_ind in range(len(rect.get_value()) - 1):
            fl = 0
            vect1 = trian.get_value()[trian_ind + 1][0] - trian.get_value()[trian_ind][0], \
                    trian.get_value()[trian_ind + 1][1] - trian.get_value()[trian_ind][1]
            vect2 = rect.get_value()[rect_ind + 1][0] - rect.get_value()[rect_ind][0], rect.get_value()[rect_ind + 1][
                1] - rect.get_value()[rect_ind][1]
            if ((vect1[0] * vect2[1]) - (vect1[1] * vect2[0])) == 0:
                continue
            else:
                fl += 1
            vect3 = rect.get_value()[rect_ind][0] - trian.get_value()[trian_ind][0], rect.get_value()[rect_ind][1] - \
                    trian.get_value()[trian_ind][1]
            t = ((vect3[0] * vect2[1]) - (vect3[1] * vect2[0])) / ((vect1[0] * vect2[1]) - (vect1[1] * vect2[0]))
            if t < 0 or t > 1:
                continue
            else:
                fl += 1
            u = ((vect3[0] * vect1[1]) - (vect3[1] * vect1[0])) / ((vect1[0] * vect2[1]) - (vect1[1] * vect2[0]))
            if u < 0 or u > 1:
                continue
            else:
                fl += 1
            if fl == 3:
                f = True
    return True if f else False


tmp = tuple()
rect_id = ""
f = False

while f == False:
    rect_id = input(
        "Введите 4 точки четырёхугольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
    lt = list(map(str, rect_id.split(' ')))
    stri = ''
    try:
        if len(lt) != 4:
            raise Uncorrect("")
        try:
            for i in range(len(lt)):
                lt[i] = lt[i].replace('(', '')
                lt[i] = lt[i].replace(')', '')
                lt[i] = lt[i].replace(' ', '')
                stri += lt[i] + ' '
            tmp = tuple([(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
            try:
                if Rect_is_Exist(tmp) != True:
                    raise Non_existence_of_rectiangle_except("Не существует такого прямоугольника!")
                f = True
            except Non_existence_of_rectiangle_except as exc:
                print(exc)
        except ValueError:
            print("Координата может быть только числом!")
    except Uncorrect as excep:
        pass

f = False
tmpi = tuple()
trian_id = ""

while f == False:
    trian_id = input("Введите 3 точки треугольника в формате: (num_x;num_y) (num_x;num_y) (num_x;num_y)\n")
    lt = list(map(str, trian_id.split(' ')))
    stri = ''
    try:
        if len(lt) != 3:
            raise Uncorrect("")
        try:
            for i in range(len(lt)):
                lt[i] = lt[i].replace('(', '')
                lt[i] = lt[i].replace(')', '')
                lt[i] = lt[i].replace(' ', '')
                stri += lt[i] + ' '
            tmpi = tuple([(float(x[0:x.find(';')]), float(x[x.find(';') + 1:len(x)])) for x in stri.split()])
            try:
                if Triangle_is_Exist(tmp) != True:
                    raise Non_existence_of_triangle_except("Не существует такого треугольника!")
                f = True
            except Non_existence_of_rectiangle_except as exc:
                print(exc)
        except ValueError:
            print("Координата может быть только числом!")
    except Uncorrect as excep:
        pass

MyRectangle = Rectangle(rect_id, tmp)
MyTriangle = Triangle(trian_id, tmpi)
MyRectangle.move()
if isIntersect(MyRectangle, MyTriangle):
    print("Пересечение фигур имеется!")
else:
    print("Пересечение фигур отсутствует!")
del MyRectangle
del MyTriangle
del Triangle
del Rectangle