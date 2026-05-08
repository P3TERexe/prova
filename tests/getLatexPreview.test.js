const test = require('node:test');
const assert = require('node:assert');
const fs = require('node:fs');
const path = require('node:path');

// Helper to extract the function from the HTML file and provide a module environment
function getFunctionFromHtml() {
    const htmlPath = path.join(__dirname, '../eq-solver.html');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');

    // Extract the script content
    const scriptRegex = /<script>([\s\S]*?)<\/script>/g;
    let match;
    let scriptContent = '';
    while ((match = scriptRegex.exec(htmlContent)) !== null) {
        if (match[1].includes('function getLatexPreview')) {
            scriptContent = match[1];
            break;
        }
    }

    if (!scriptContent) {
        throw new Error('Could not find script containing getLatexPreview in eq-solver.html');
    }

    // Create a mock environment for the script
    const mockModule = { exports: {} };
    const mockDocument = {
        getElementById: () => ({ addEventListener: () => {} }),
        createElement: () => ({ appendChild: () => {} })
    };
    const mockWindow = {
        addEventListener: () => {},
        location: { hash: '' },
        history: { replaceState: () => {} },
        matchMedia: () => ({ matches: false })
    };
    const mockLocalStorage = {
        getItem: () => null,
        setItem: () => {}
    };

    // Execute the script in a restricted scope
    const fn = new Function('module', 'document', 'window', 'localStorage', 'navigator', 'katex', scriptContent);

    try {
        fn(mockModule, mockDocument, mockWindow, mockLocalStorage, {}, {});
    } catch (e) {
        // We expect some errors because we are not in a full browser env,
        // but getLatexPreview should be defined by now.
    }

    if (mockModule.exports.getLatexPreview) {
        return mockModule.exports.getLatexPreview;
    }

    // Fallback if the export didn't work as expected in the mock env
    const functionRegex = /function getLatexPreview\(str\) \{([\s\S]*?)\}/;
    const funcMatch = scriptContent.match(functionRegex);
    return new Function('str', funcMatch[1]);
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

test('getLatexPreview should handle parentheses and multiplication', () => {
    assert.strictEqual(getLatexPreview('(a+b)*c'), '(a+b)\\cdot c');
});

test('getLatexPreview should handle mixed operations', () => {
    assert.strictEqual(getLatexPreview('x**2 + 2*x'), 'x^2 + 2\\cdot x');
});

test('getLatexPreview should handle overlapping patterns correctly', () => {
    assert.strictEqual(getLatexPreview('x***3'), 'x^\\cdot 3');
});

test('getLatexPreview should return empty string if input is empty', () => {
    assert.strictEqual(getLatexPreview(''), '');
});

test('getLatexPreview should return the same string if no replacements are needed', () => {
    assert.strictEqual(getLatexPreview('x + y - z / 2'), 'x + y - z / 2');
});
