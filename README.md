# Results

|Substring                                | Boyer–Moore          | Knuth–Morris–Pratt   | Rabin-Karp           |
|---------------------------------------- | -------------------- | -------------------- | -------------------- |
|public static int binarySearch           |              0.00010 |              0.00061 |              0.00181 |
|Strawberry is my favorite fruit          |              0.00027 |              0.00178 |              0.00527 |
|A comparison of current graph            |              0.00034 |              0.00241 |              0.00892 |
|Also, I love black tea                   |              0.00048 |              0.00271 |              0.00765 |


У даній таблиці були представлені результати часу виконання для трьох алгоритмів пошуку рядків: Boyer–Moore, Knuth–Morris–Pratt і Rabin-Karp. Для аналізу цих алгоритмів було використано два тексти і підрядки з колонки "Substring" (чергуючи існуючі та неіснуючі у кожному з текстів). Результати аналізу показують, як кожен алгоритм впорався з пошуком цих слів.

**Висновки:**

- *Boyer–Moore* виявився найшвидшим алгоритмом у всіх випадках, швидко знаходячи навіть великі слова.
- *Knuth–Morris–Pratt* зазвичай був повільнішим за Boyer–Moore, але краще за Rabin-Karp, особливо на коротших словах.
- *Rabin-Karp* демонструє відносно стабільну, але меншу швидкість порівняно з іншими алгоритмами, особливо на великих текстах.

Отже, якщо маємо справу з великими текстами та потрібно швидко знаходити слова, **Boyer–Moore** може бути кращим вибором. Однак для коротких слів інші алгоритми також можуть бути ефективними.