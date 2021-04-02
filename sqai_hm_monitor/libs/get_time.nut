
class get_time_cmd {
  // 今の時間を返す
  function exec(str) {
    local time = world.get_time()
    local f = file(path_output,"w")
	time.month += 1
    f.writestr("現在の日付は" + time.year + "年" + time.month + "月です。")
    f.close() 
  }
}
