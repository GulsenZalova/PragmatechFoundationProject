1. Javascriptd keçmediyimiz məlumat növləri və onlar haqqında məlumat:
a) JavaScript Objects
Javascriptdə obyekt məlumat növləri bəzəkli mötərizə {} daxilində yazılır.Burada obyektin xassələrinin adları və bu xassələrə verilən dəyərlər qeyd olunur.Onlar bir-birindən qoşa nöqtə ilə ayrılır və dəyərlər dırnaq içərisində yazılır.Obyektin hansısa xassəsinə müraciət etmək üçün obyektin adə, "nöqtə işərəsi" və xassənin adı yazılmalıdır.
const car={color:"white", model:"Toyoto",} 
müraciət forması: car.color

b) JavaScript Array
Javascriptdə Array məlumat növləri  kvadrat mötərizə [] daxilində yazılır. Burada bir neçə elementi eyni anda yazmaq olur. Onlar bir-birindən vergül ilə ayrılır, elementlerin sırası 1-dən deyil sıfırdan başlayır, yəni birinci elementə müraciəti 0 yazaraq etmək lazımdır.
const ad=["Gülşən", "Aytac", "Nurlan"]
Burada Gülşənə müraciət etmək üçün ad.(0) yazmaq lazımdır.


2. Funksiyaların təyin olunma üslubları:
Funksiyanın ümumi sintaksisi belədir- funksiya açar sözü, funksiyanın adı (parapetrlər){kod bloku}. Funksiyaların təyin olunma üslublarındakı fərq parametrlərin verilib-verilməməyi ilə əlaqədardır.
a)Parametrsiz funksiyalar. 
<script>
function myfunction(){
let a=5
let b=6
document.write(a*b)
}
myfunction
</script>

b)Parametrli funksiyalar
<script>
function hesabla(x1,x2){
alert(x1*x2)
hesabla(3,4)
}

</script>

3. Functional scope,Local scope, Block scope və Global scope anlayışları haqqında məlumat:
Functional scope : Yazılan kodlar ancaq funksiya daxilində keçərlidir.
Block scope : Bəzəkli mötərizə daxilində yazılan kodlardır. Bunlara let və const variableları aiddir.
Local scope : Lokal xarakter daşıyır və yazılan kodlar ancaq səhifənin təyin olunmuş hissəsində görünə bilir. Const və let buraya aiddir. Yəni biz əgər bunları lokalda təyin etsək səhifənin hər yerində görə bilmərik. 

<script>

 if(true){
    let a=5
    alert(a)
 }
 <!-- bu sehifede gorunecek -->

 if(true){
    let a=5
 }
 alert(a)
<!-- bu sehifede gorunmeyecek -->
<!-- Cunki let lokal scope-dur ve lokalda teyin edildikden sonra onu qlobalda gormek olmur, globalda teyin etsek lokalda rahatliqla gormek olar. Eyni xassə const ucun de kecerlidir. -->
Global scope : Qlobal xarakter daşıyır və kodun harada yazılmasından asılı olmayaraq, sehifeinin her yerine gorune bilir. Buraya var variable aiddir.

if(true){
    var ad="Gülşən"
    alert(ad)
}

if(true){
    var ad="Gülşən"  
} 
alert(ad)
<!-- her ikisinde de verilen deyer gorunecek -->

</>