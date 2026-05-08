const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');

// Helper to extract the function from the HTML file
function getFunctionFromHtml() {
    const htmlPath = path.join(__dirname, '../eq-solver.html');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');

    // Extract the function using regex
    const regex = /function getLatexPreview\(str\) \{([\s\S]*?)\}/;
    const match = htmlContent.match(regex);

    if (!match) {
        throw new Error('Could not find getLatexPreview function in eq-solver.html');
    }

    // Create the function dynamically
    return new Function('str', match[1]);
}

const getLatexPreview = getFunctionFromHtml();

test('getLatexPreview should replace ** with ^', () => {
    assert.strictEqual(getLatexPreview('x**2'), 'x^2');
    assert.strictEqual(getLatexPreview('x**2 + y**3'), 'x^2 + y^3');
});

test('getLatexPreview should replace * with \\cdot ', () => {
    assert.strictEqual(getLatexPreview('2*x'), '2\\cdot x');
    assert.strictEqual(getLatexPreview('x*y*z'), 'x\\cdot y\\cdot z');
});

test('getLatexPreview should handle both replacements correctly', () => {
    assert.strictEqual(getLatexPreview('2*x**2 + 3*x + 1'), '2\\cdot x^2 + 3\\cdot x + 1');
});

test('getLatexPreview should handle overlapping patterns correctly', () => {
    // Current implementation: s = s.replace(/\*\*/g, '^'); s = s.replace(/\*/g, '\\cdot ');
    // So x***3 should become x^\\cdot 3
    assert.strictEqual(getLatexPreview('x***3'), 'x^\\cdot 3');
});

test('getLatexPreview should return empty string if input is empty', () => {
    assert.strictEqual(getLatexPreview(''), '');
});

test('getLatexPreview should return the same string if no replacements are needed', () => {
    assert.strictEqual(getLatexPreview('x + y - z / 2'), 'x + y - z / 2');
});
