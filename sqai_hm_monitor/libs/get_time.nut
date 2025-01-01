// メッセージ定義
local text_time = "現在の日付は%d年%d月です。\n時刻は%02d:%02d:%02dです。"

include("libs/embed_out")
class get_time_cmd {
  // 今の時間を返す
  function exec(str) {
    local time = world.get_time()
	  time.month += 1
    // 現在のtick数から次の月が始まるタイミングのtickを引き、次の月までの所要tick数(マイナス)を出す。
    // 次の月までの所要tick数(マイナス)に月あたりのtick数を足すと、月が始まってからのtick数が出てくる。
    local ticks_of_month = time.ticks - time.next_month_ticks + time.ticks_per_month
    local hour = ticks_of_month * 24 / time.ticks_per_month
    local minute = ticks_of_month * 24 * 60 / time.ticks_per_month % 60
    local second = ticks_of_month * 24 * 60 * 60 / time.ticks_per_month % 60 % 60
    embed_normal(format(text_time, time.year, time.month, hour, minute, second))
  }
}
