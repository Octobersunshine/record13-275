from datetime import datetime
from typing import Union, Dict, Optional
from dateutil.relativedelta import relativedelta


class DateService:
    DATE_FORMAT = "%Y-%m-%d"

    _CN_WEEKDAYS = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    FORMAT_PRESETS: Dict[str, str] = {
        "iso": "%Y-%m-%d",
        "cn": "%Y年%m月%d日",
        "us": "%m/%d/%Y",
        "eu": "%d.%m.%Y",
        "slash": "%Y/%m/%d",
        "compact": "%Y%m%d",
        "long_cn": "%Y年%m月%d日",
        "timestamp": "%Y-%m-%d %H:%M:%S",
    }

    @classmethod
    def _parse_date(cls, date_str: Union[str, datetime]) -> datetime:
        if isinstance(date_str, datetime):
            return date_str
        if isinstance(date_str, str):
            return datetime.strptime(date_str, cls.DATE_FORMAT)
        raise TypeError(f"Unsupported date type: {type(date_str)}")

    @classmethod
    def _resolve_format(cls, fmt: str) -> str:
        if fmt in cls.FORMAT_PRESETS:
            return cls.FORMAT_PRESETS[fmt]
        return fmt

    @classmethod
    def format_date(cls, date: Union[str, datetime], fmt: str = "iso") -> str:
        dt = cls._parse_date(date)
        if fmt == "long_cn":
            return f"{dt.strftime(cls.FORMAT_PRESETS['long_cn'])}{cls._CN_WEEKDAYS[dt.weekday()]}"
        return dt.strftime(cls._resolve_format(fmt))

    @classmethod
    def format_all(cls, date: Union[str, datetime]) -> Dict[str, str]:
        dt = cls._parse_date(date)
        results = {}
        for name, pattern in cls.FORMAT_PRESETS.items():
            if name == "long_cn":
                results[name] = f"{dt.strftime(pattern)}{cls._CN_WEEKDAYS[dt.weekday()]}"
            else:
                results[name] = dt.strftime(pattern)
        return results

    @classmethod
    def _output(cls, dt: datetime, output_format: Optional[str] = None) -> str:
        if output_format is None:
            return dt.strftime(cls.DATE_FORMAT)
        if output_format == "long_cn":
            return f"{dt.strftime(cls.FORMAT_PRESETS['long_cn'])}{cls._CN_WEEKDAYS[dt.weekday()]}"
        return dt.strftime(cls._resolve_format(output_format))

    @classmethod
    def add_days(cls, date: Union[str, datetime], days: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(days=days)
        return cls._output(result, output_format)

    @classmethod
    def subtract_days(cls, date: Union[str, datetime], days: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(days=days)
        return cls._output(result, output_format)

    @classmethod
    def add_months(cls, date: Union[str, datetime], months: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(months=months)
        return cls._output(result, output_format)

    @classmethod
    def subtract_months(cls, date: Union[str, datetime], months: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(months=months)
        return cls._output(result, output_format)

    @classmethod
    def add_years(cls, date: Union[str, datetime], years: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(years=years)
        return cls._output(result, output_format)

    @classmethod
    def subtract_years(cls, date: Union[str, datetime], years: int, output_format: Optional[str] = None) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(years=years)
        return cls._output(result, output_format)

    @classmethod
    def days_between(cls, date1: Union[str, datetime], date2: Union[str, datetime]) -> int:
        dt1 = cls._parse_date(date1)
        dt2 = cls._parse_date(date2)
        return (dt2 - dt1).days

    @classmethod
    def detailed_diff(cls, date1: Union[str, datetime], date2: Union[str, datetime]) -> Dict[str, int]:
        dt1 = cls._parse_date(date1)
        dt2 = cls._parse_date(date2)
        delta = relativedelta(dt2, dt1)
        return {
            "years": delta.years,
            "months": delta.months,
            "days": delta.days,
        }


def main():
    presets = list(DateService.FORMAT_PRESETS.keys())

    print("=== 日期计算服务 ===")
    print("1. 日期加 N 天")
    print("2. 日期减 N 天")
    print("3. 日期加 N 月")
    print("4. 日期减 N 月")
    print("5. 日期加 N 年")
    print("6. 日期减 N 年")
    print("7. 计算两个日期相差天数")
    print("8. 计算两个日期相差（年/月/日）")
    print("9. 日期格式化（单格式）")
    print("10. 日期格式化（全格式预览）")
    print("0. 退出")

    while True:
        choice = input("\n请选择操作 (0-10): ").strip()

        try:
            if choice == "1":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                days = int(input("请输入要加的天数: ").strip())
                result = DateService.add_days(date, days)
                print(f"{date} + {days} 天 = {result}")

            elif choice == "2":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                days = int(input("请输入要减的天数: ").strip())
                result = DateService.subtract_days(date, days)
                print(f"{date} - {days} 天 = {result}")

            elif choice == "3":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                months = int(input("请输入要加的月数: ").strip())
                result = DateService.add_months(date, months)
                print(f"{date} + {months} 月 = {result}")

            elif choice == "4":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                months = int(input("请输入要减的月数: ").strip())
                result = DateService.subtract_months(date, months)
                print(f"{date} - {months} 月 = {result}")

            elif choice == "5":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                years = int(input("请输入要加的年数: ").strip())
                result = DateService.add_years(date, years)
                print(f"{date} + {years} 年 = {result}")

            elif choice == "6":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                years = int(input("请输入要减的年数: ").strip())
                result = DateService.subtract_years(date, years)
                print(f"{date} - {years} 年 = {result}")

            elif choice == "7":
                date1 = input("请输入第一个日期 (YYYY-MM-DD): ").strip()
                date2 = input("请输入第二个日期 (YYYY-MM-DD): ").strip()
                diff = DateService.days_between(date1, date2)
                print(f"两个日期相差 {diff} 天")

            elif choice == "8":
                date1 = input("请输入第一个日期 (YYYY-MM-DD): ").strip()
                date2 = input("请输入第二个日期 (YYYY-MM-DD): ").strip()
                diff = DateService.detailed_diff(date1, date2)
                print(f"两个日期相差 {diff['years']} 年 {diff['months']} 月 {diff['days']} 天")

            elif choice == "9":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                print(f"可用格式: {', '.join(presets)}，或输入自定义 strftime 格式")
                fmt = input("请输入格式名称或格式串: ").strip()
                result = DateService.format_date(date, fmt)
                print(f"格式化结果: {result}")

            elif choice == "10":
                date = input("请输入日期 (YYYY-MM-DD): ").strip()
                results = DateService.format_all(date)
                print(f"日期 {date} 的全格式预览:")
                for name, value in results.items():
                    print(f"  {name:12s} -> {value}")

            elif choice == "0":
                print("再见!")
                break

            else:
                print("无效选择，请重新输入。")

        except (ValueError, TypeError) as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    main()
