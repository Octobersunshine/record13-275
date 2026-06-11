from datetime import datetime
from typing import Union, Dict
from dateutil.relativedelta import relativedelta


class DateService:
    DATE_FORMAT = "%Y-%m-%d"

    @classmethod
    def _parse_date(cls, date_str: Union[str, datetime]) -> datetime:
        if isinstance(date_str, datetime):
            return date_str
        if isinstance(date_str, str):
            return datetime.strptime(date_str, cls.DATE_FORMAT)
        raise TypeError(f"Unsupported date type: {type(date_str)}")

    @classmethod
    def add_days(cls, date: Union[str, datetime], days: int) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(days=days)
        return result.strftime(cls.DATE_FORMAT)

    @classmethod
    def subtract_days(cls, date: Union[str, datetime], days: int) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(days=days)
        return result.strftime(cls.DATE_FORMAT)

    @classmethod
    def add_months(cls, date: Union[str, datetime], months: int) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(months=months)
        return result.strftime(cls.DATE_FORMAT)

    @classmethod
    def subtract_months(cls, date: Union[str, datetime], months: int) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(months=months)
        return result.strftime(cls.DATE_FORMAT)

    @classmethod
    def add_years(cls, date: Union[str, datetime], years: int) -> str:
        dt = cls._parse_date(date)
        result = dt + relativedelta(years=years)
        return result.strftime(cls.DATE_FORMAT)

    @classmethod
    def subtract_years(cls, date: Union[str, datetime], years: int) -> str:
        dt = cls._parse_date(date)
        result = dt - relativedelta(years=years)
        return result.strftime(cls.DATE_FORMAT)

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
    print("=== 日期计算服务 ===")
    print("1. 日期加 N 天")
    print("2. 日期减 N 天")
    print("3. 日期加 N 月")
    print("4. 日期减 N 月")
    print("5. 日期加 N 年")
    print("6. 日期减 N 年")
    print("7. 计算两个日期相差天数")
    print("8. 计算两个日期相差（年/月/日）")
    print("9. 退出")

    while True:
        choice = input("\n请选择操作 (1-9): ").strip()

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
                print("再见!")
                break

            else:
                print("无效选择，请重新输入。")

        except (ValueError, TypeError) as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    main()
