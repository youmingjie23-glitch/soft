from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="相親配對系統")

templates = Jinja2Templates(directory="templates")

# 模擬會員資料
PROFILES = [
    {"id": 1, "name": "陳小美", "gender": "女", "age": 25, "occupation": "UI/UX 設計師", "bio": "喜歡看展覽、喝咖啡，尋找有幽默感的另一半。"},
    {"id": 2, "name": "林大衛", "gender": "男", "age": 28, "occupation": "軟體工程師", "bio": "熱愛戶外運動與 Vibe Coding，希望能找到一起旅行的夥伴。"},
    {"id": 3, "name": "張雅婷", "gender": "女", "age": 27, "occupation": "鋼琴教師", "bio": "平時喜歡彈琴與貓咪，性格溫和好相處。"}
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "profiles": PROFILES})

@app.get("/api/profiles")
async def get_profiles():
    return {"status": "success", "data": PROFILES}
