import fetch_stats
import app
import sys

def main():
    fetch_stats.run()
    app.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ 抓取失败：{e}")
        sys.exit(1)