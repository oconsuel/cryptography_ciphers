const abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", t = {};
for (let i = 0, j = abc.length; j;) t[abc.charAt(i++)] = abc.charAt(--j);
const atbash = s => s ? (t[s.charAt(0)] || s.charAt(0)) + atbash(s.slice(1)) : s;

let text = 'привет мир \n';

let text2 = 'Вот пример статьи на тысячу символов. Это достаточно маленький текст, оптимально подходящий для карточек товаров в интернет или магазинах или для небольших информационных публикаций. В таком тексте редко бывает более двух или трёх абзацев и обычно один подзаголовок. Но можно и без него. На тысячу символов рекомендовано использовать один или два ключа и одну картину. Текст на тысячу символов это сколько примерно слов? Статистика показывает, что тысяча включает в себя стопятьдесят или двести слов средней величины. Но, если злоупотреблять предлогами, союзами и другими частями речи на один или два символа, то количество слов неизменно возрастает. В копирайтерской деятельности принято считать тысячи с пробелами или без. Учет пробелов увеличивает объем текста примерно на сто или двести символов именно столько раз мы разделяем слова свободным пространством. Считать пробелы заказчики не любят, так как это пустое место. Однако некоторые фирмы и биржи видят справедливым ставить стоимость за тысячу символов с пробелами, считая последние важным элементом качественного восприятия. Согласитесь, читать слитный текст без единого пропуска, никто не будет. Но большинству нужна цена за тысячу знаков без пробелов. \n'

let text3 = 'Красивыми словами пастернак не помаслишь \n'

let enc1 = atbash(text)
let dec1 = atbash(enc1)

let enc2 = atbash(text2)
let dec2 = atbash(enc2)

let enc3 = atbash(text3)
let dec3 = atbash(enc3)


console.log(enc1);
console.log(dec1);

console.log(enc2);
console.log(dec2);

console.log(enc3);
console.log(dec3);



