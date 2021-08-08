const fruits_into_baskets = (fruits) => {
    let result = 0;
    let baskets = new Map();
    let fruitsInBaskets = 0;

    for (let i = 0; i < fruits.length; i++) {
        baskets.set(fruits[i], (baskets.get(fruits[i]) || 0) + 1)
        fruitsInBaskets++;
        while (baskets.size > 2){
            const initial = fruits[i - --fruitsInBaskets]
            initial && baskets.set(initial, (baskets.get(initial)) - 1);
            !baskets.get(initial) && baskets.delete(initial)
        }
        result = Math.max(fruitsInBaskets, result);
    }

    return result;
};

console.log(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])); // 3
console.log(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])); // 5
