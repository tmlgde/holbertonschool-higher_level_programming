#!/usr/bin/node

const args = process.argv.slice(2)

if (args.lenght === 0) {
    console.log('No argument');
} else if (args.lenght === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}