// メッセージ定義
local text_time = "現在の日付は%d年%d月です。"

include("libs/embed_out")
class get_time_cmd {
  // 今の時間を返す
  function exec(str) {
    local time = world.get_time()
	  time.month += 1
    embed_normal(format(text_time, time.year, time.month))
  }
}
