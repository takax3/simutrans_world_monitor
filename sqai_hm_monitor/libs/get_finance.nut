// メッセージ定義
local text_title = "各会社の資金は次の通りです。\n"
local text_money_info = "%s:  %s￠\n"

include("libs/common")

class get_finances_cmd {
  // 各プレイヤーの手持ち資金を返す
  function exec(str) {
    local idx = 1
    local str = text_title
    foreach (player in get_player_list()) {
	  local cash = _comma_separate(format("%.f",player.get_current_cash()))
      str += format(text_money_info, player.get_name(), cash)
      idx += 1
    }
    local f = file(path_output,"w")
    f.writestr(rstrip(str))
    f.close() 
  }
}