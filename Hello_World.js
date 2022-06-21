function hello_world_one(phrase_one, phrase_two) {
    console.log(phrase_one);
    console.log(phrase_two);
}
hello_world_one("Hello World in JavaScript!", " - moves to next line after phrase");

function hello_world_two(phrase_one, phrase_two) {
    process.stdout.write(phrase_one);
    process.stdout.write(phrase_two);
}
hello_world_two("Hello World in JavaScript!", " - does not move to next line after phrase");