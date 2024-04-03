// usando pre-processadores (#define)
#define LENGTH 10
#define WIDTH 5
#define NEWLINE '\n'

int main() {
    int area;
    area = LENGTH * WIDTH;
    NSLog(@"valod da área: %d", area);
    NSLog(@"%c", NEWLINE);

    return 0;
}