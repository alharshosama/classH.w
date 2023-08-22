# الاسم:اسامة محمد الهرش
#Class and Static methods شرح نبذة  ماالفرق بين
#statice من المعروف أن أي دالة تصف ب 
# تكون تنتمي للصنف و ليس لاوبجت من ذلك الصنف بما معناه إننا نستطيع إستدعاء الدالة فقط بكتابة إسم الصنف دون عملinstance 
# منه أي خلق أوبجت كالتالي 
class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")

#هنا نقوم بخلق أوبجكت أو وحده من هذا الصنف 
a = A()

#يمكننا هنا أستدعاء الclassmethod 
#بهذه الطريقة فقط 
a.class_foo(1)

# static_fooأما ال
#فهي تنتمي فقط للكلاس و ليس للأوبجت لذلك يتم أستدعائها من عن طريق إسم الكلاس 
#كالتالي 
A.static_foo('hi')



# مثال اخر
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # دالة ساكنة لاختبار فيما إذا كان مسناً أم لا
    @staticmethod
    def old(age):
        print("old")
        return age > 55

    #person كلاس ميثود لإنشاء كائن من الصف 
    @classmethod
    def create(cls, name, year):
        return cls(name, date.today().year - year)

print (Person.old(22)) # True
obj=Person.create('km',24)
print(obj)  #  <__main__.Person object at 0x000001C7DC405708>
obj.age # 1997

# classmethodكما أن ال 
# staticmethodتمكنك من تغيير الجالة للأوبجكت ال 
# لا تستطيع بها أنم تقوم بتغيير أي حالة و ليس لها علم بأي معلومات عن الأوبجكت 
# cls تاخذclassmethos و كما نرى 
#staticmethod كمتغير يمرر اليها و يجب تمريره أما ال
# فليس شرط أن تأخذ أي متغير 
