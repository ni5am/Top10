<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# A10:2025 예외 조건 처리 오류 (Mishandling of Exceptional Conditions)

## 배경 (Background). 

예외 조건 처리 오류는 2025년의 새로운 카테고리입니다. 이 카테고리는 24개의 CWE를 포함하며 부적절한 오류 처리, 논리 오류, 실패 시 열림(failing open), 그리고 시스템이 마주칠 수 있는 비정상적인 조건에서 비롯된 기타 관련 시나리오에 초점을 맞춥니다. 이 카테고리에는 이전에 낮은 코드 품질과 관련된 일부 CWE가 있습니다. 그것은 우리에게 너무 일반적이었습니다. 우리의 의견으로는, 이 더 구체적인 카테고리가 더 나은 가이드를 제공합니다.

이 카테고리에 포함된 주목할 만한 CWE: *CWE-209 민감한 정보를 포함하는 오류 메시지 생성 (Generation of Error Message Containing Sensitive Information), CWE-234 누락된 매개변수 처리 실패 (Failure to Handle Missing Parameter), CWE-274 불충분한 권한의 부적절한 처리 (Improper Handling of Insufficient Privileges), CWE-476 NULL 포인터 역참조 (NULL Pointer Dereference)*, *CWE-636 안전하게 실패하지 않음 ('실패 시 열림', Not Failing Securely ('Failing Open'))*


## 점수 표 (Score table).


<table>
  <tr>
   <td>매핑된 CWE (CWEs Mapped) 
   </td>
   <td>최대 발생률 (Max Incidence Rate)
   </td>
   <td>평균 발생률 (Avg Incidence Rate)
   </td>
   <td>최대 커버리지 (Max Coverage)
   </td>
   <td>평균 커버리지 (Avg Coverage)
   </td>
   <td>평균 가중 악용 (Avg Weighted Exploit)
   </td>
   <td>평균 가중 영향 (Avg Weighted Impact)
   </td>
   <td>총 발생 횟수 (Total Occurrences)
   </td>
   <td>총 CVE (Total CVEs)
   </td>
  </tr>
  <tr>
   <td>24
   </td>
   <td>20.67%
   </td>
   <td>2.95%
   </td>
   <td>100.00%
   </td>
   <td>37.95%
   </td>
   <td>7.11
   </td>
   <td>3.81
   </td>
   <td>769,581
   </td>
   <td>3,416
   </td>
  </tr>
</table>



## 설명 (Description). 

소프트웨어에서 예외 조건 처리 오류는 프로그램이 비정상적이고 예측할 수 없는 상황을 방지, 탐지 및 대응하는 데 실패하여 크래시, 예상치 못한 동작, 때로는 취약점으로 이어지는 경우 발생합니다. 이것은 다음 3가지 실패 중 하나 이상을 포함할 수 있습니다. 애플리케이션이 비정상적인 상황이 발생하는 것을 방지하지 않거나, 상황이 발생하는 것을 식별하지 않거나, 그 이후에 상황에 대해 잘못 대응하거나 전혀 대응하지 않습니다.

 

예외 조건은 누락되거나 나쁘거나 불완전한 입력 검증, 또는 발생하는 함수에서 늦은 고수준 오류 처리 대신, 메모리, 권한 또는 네트워크 문제와 같은 예상치 못한 환경 상태, 일관성 없는 예외 처리, 또는 전혀 처리되지 않는 예외로 인해 발생할 수 있으며, 시스템이 알 수 없고 예측할 수 없는 상태로 떨어지도록 허용합니다. 애플리케이션이 다음 명령에 대해 확실하지 않은 경우, 예외 조건이 잘못 처리되었습니다. 찾기 어려운 오류와 예외는 오랫동안 전체 애플리케이션의 보안을 위협할 수 있습니다.

 

예외 조건을 잘못 처리할 때 많은 다른 보안 취약점이 발생할 수 있습니다.

논리 버그, 오버플로우, 경쟁 조건, 사기 거래, 또는 메모리, 상태, 리소스, 타이밍, 인증 및 인증과 관련된 문제와 같은 것들입니다. 이러한 유형의 취약점은 시스템 또는 데이터의 기밀성, 가용성 및/또는 무결성에 부정적인 영향을 줄 수 있습니다. 공격자는 애플리케이션의 결함이 있는 오류 처리를 조작하여 이 취약점을 공격합니다. 


## 예방 방법 (How to prevent). 

예외 조건을 적절하게 처리하려면 그러한 상황을 계획해야 합니다(최악을 기대하세요). 발생하는 장소에서 직접 모든 가능한 시스템 오류를 '잡아야(catch)' 하고 그것을 처리해야 합니다(문제를 해결하고 문제로부터 복구하도록 의미 있는 일을 하는 것을 의미). 처리의 일부로, 오류를 발생시키는 것(사용자에게 이해할 수 있는 방식으로 알리기), 이벤트 로깅, 그리고 정당하다고 느끼는 경우 알림 발행을 포함해야 합니다. 또한 놓친 것이 있을 경우를 대비해 전역 예외 핸들러를 두어야 합니다. 이상적으로는, 지속적인 공격을 나타내는 반복된 오류나 패턴을 감시하고 어떤 종류의 응답, 방어 또는 차단을 발행할 수 있는 모니터링 및/또는 관찰 가능성 도구나 기능도 갖고 싶을 것입니다. 이것은 오류 처리 약점에 초점을 맞추는 스크립트와 봇을 차단하고 대응하는 데 도움이 될 수 있습니다.

 

예외 조건을 잡고 처리하는 것은 프로그램의 기본 인프라가 예측할 수 없는 상황을 처리하도록 남겨지지 않도록 보장합니다. 어떤 종류의 거래 중간에 있다면, 거래의 모든 부분을 롤백하고 다시 시작하는 것이 극히 중요합니다(닫힌 상태로 실패(failing closed)라고도 함). 거래 중간에 거래를 복구하려는 시도는 종종 복구할 수 없는 실수를 만드는 곳입니다.

 

가능할 때마다, 첫 번째 장소에서 예외 조건을 방지하기 위해 속도 제한, 리소스 할당량, 스로틀링 및 기타 제한을 가능한 한 추가하세요. 정보 기술에는 무제한인 것이 없어야 합니다. 이것은 애플리케이션 복원력 부족, 서비스 거부, 성공적인 무차별 대입 공격, 그리고 엄청난 클라우드 청구서로 이어집니다. \
특정 비율 이상의 동일한 반복 오류는 발생한 빈도와 시간 프레임을 보여주는 통계로만 출력되어야 하는지 고려하세요. 이 정보는 자동화된 로깅 및 모니터링을 방해하지 않도록 원본 메시지에 추가되어야 합니다. A09:2025 로깅 및 알림 실패 (Logging & Alerting Failures) TJ를 참조하세요.

 

이 위에, 우리는 엄격한 입력 검증(수용해야 하는 잠재적으로 위험한 문자에 대한 정제 또는 이스케이프 포함), 그리고 *중앙화된* 오류 처리, 로깅, 모니터링 및 알림, 그리고 전역 예외 핸들러를 포함하고 싶을 것입니다. 하나의 애플리케이션은 예외 조건을 처리하기 위한 여러 함수를 가져서는 안 되며, 한 곳에서 매번 같은 방식으로 수행되어야 합니다. 우리는 또한 이 섹션의 모든 조언에 대한 프로젝트 보안 요구 사항을 만들어야 하며, 프로젝트의 설계 단계에서 위협 모델링 및/또는 안전한 설계 검토 활동을 수행하고, 코드 검토 또는 정적 분석을 수행하며, 최종 시스템의 스트레스, 성능 및 침투 테스트를 실행해야 합니다.

 

가능한 경우, 전체 조직이 같은 방식으로 예외 조건을 처리해야 합니다. 이것은 이 중요한 보안 제어에서 오류에 대한 코드를 검토하고 감사하기 쉽게 만듭니다.


## 공격 시나리오 예 (Example attack scenarios). 

**FIXME**: 예제를 더 현대적으로 업데이트

**시나리오 #1:** 예외 조건 처리 오류를 통한 리소스 고갈(서비스 거부)은 파일이 업로드될 때 애플리케이션이 예외를 잡지만 그 후에 리소스를 적절하게 해제하지 않는 경우 발생할 수 있습니다. 각 새로운 예외는 모든 리소스가 소진될 때까지 리소스를 잠그거나 그렇지 않으면 사용할 수 없게 만듭니다.

**시나리오 #2:** 부적절한 처리 또는 데이터베이스 오류를 통한 민감한 데이터 노출은 사용자에게 전체 시스템 오류를 공개합니다. 공격자는 더 나은 SQL 인젝션 공격을 만들기 위해 민감한 시스템 정보를 사용하기 위해 오류를 계속 강제합니다. 사용자 오류 메시지의 민감한 데이터는 정찰입니다. 

**시나리오 #3:** 금융 거래의 상태 손상은 공격자가 네트워크 중단을 통해 다단계 거래를 방해하는 경우 발생할 수 있습니다. 거래 순서가 다음과 같다고 상상해보세요: 사용자 계정 차변, 대상 계정 대변, 거래 로깅. 시스템이 중간에 오류가 있을 때 전체 거래를 적절하게 롤백하지 않으면(닫힌 상태로 실패), 공격자는 잠재적으로 사용자의 계정을 고갈시키거나 공격자가 대상에 여러 번 돈을 보낼 수 있는 경쟁 조건을 만들 수 있습니다.


## 참고 자료 (References). 

OWASP MASVS‑RESILIENCE

- [OWASP 치트 시트: 로깅 (OWASP Cheat Sheet: Logging)](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- [OWASP 치트 시트: 오류 처리 (OWASP Cheat Sheet: Error Handling)](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- [OWASP 애플리케이션 보안 검증 표준 (ASVS): V16.5 오류 처리 (OWASP Application Security Verification Standard (ASVS): V16.5 Error Handling)](https://github.com/OWASP/ASVS/blob/master/5.0/en/0x25-V16-Security-Logging-and-Error-Handling.md#v165-error-handling)

- [OWASP 테스트 가이드: 4.8.1 오류 처리 테스트 (OWASP Testing Guide: 4.8.1 Testing for Error Handling)](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/01-Testing_For_Improper_Error_Handling)

* [예외에 대한 모범 사례 (Microsoft, .Net) (Best practices for exceptions (Microsoft, .Net))](https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions)

* [클린 코드와 예외 처리의 예술 (Toptal) (Clean Code and the Art of Exception Handling (Toptal))](https://www.toptal.com/developers/abap/clean-code-and-the-art-of-exception-handling)

* [일반 오류 처리 규칙 (Google for Developers) (General error handling rules (Google for Developers))](https://developers.google.com/tech-writing/error-messages/error-handling)

## 매핑된 CWE 목록 (List of Mapped CWEs)
* [CWE-209	민감한 정보를 포함하는 오류 메시지 생성 (Generation of Error Message Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/209.html)
* [CWE-215	디버깅 코드에 민감한 정보 삽입 (Insertion of Sensitive Information Into Debugging Code)](https://cwe.mitre.org/data/definitions/215.html)
* [CWE-234	누락된 매개변수 처리 실패 (Failure to Handle Missing Parameter)](https://cwe.mitre.org/data/definitions/234.html)
* [CWE-235	추가 매개변수의 부적절한 처리 (Improper Handling of Extra Parameters)](https://cwe.mitre.org/data/definitions/235.html)
* [CWE-248	잡히지 않은 예외 (Uncaught Exception)](https://cwe.mitre.org/data/definitions/248.html)
* [CWE-252	검사되지 않은 반환 값 (Unchecked Return Value)](https://cwe.mitre.org/data/definitions/252.html)
* [CWE-274	불충분한 권한의 부적절한 처리 (Improper Handling of Insufficient Privileges)](https://cwe.mitre.org/data/definitions/274.html)
* [CWE-280	불충분한 권한 또는 특권의 부적절한 처리 (Improper Handling of Insufficient Permissions or Privileges)](https://cwe.mitre.org/data/definitions/280.html)
* [CWE-369	0으로 나누기 (Divide By Zero)](https://cwe.mitre.org/data/definitions/369.html)
* [CWE-390	조치 없는 오류 조건 탐지 (Detection of Error Condition Without Action)](https://cwe.mitre.org/data/definitions/390.html)
* [CWE-391	검사되지 않은 오류 조건 (Unchecked Error Condition)](https://cwe.mitre.org/data/definitions/391.html)
* [CWE-394	예상치 못한 상태 코드 또는 반환 값 (Unexpected Status Code or Return Value)](https://cwe.mitre.org/data/definitions/394.html)
* [CWE-396	일반 예외에 대한 Catch 선언 (Declaration of Catch for Generic Exception)](https://cwe.mitre.org/data/definitions/396.html)
* [CWE-397	일반 예외에 대한 Throws 선언 (Declaration of Throws for Generic Exception)](https://cwe.mitre.org/data/definitions/397.html)
* [CWE-460	발생한 예외에 대한 부적절한 정리 (Improper Cleanup on Thrown Exception)](https://cwe.mitre.org/data/definitions/460.html)
* [CWE-476	NULL 포인터 역참조 (NULL Pointer Dereference)](https://cwe.mitre.org/data/definitions/476.html)
* [CWE-478	다중 조건 표현식에서 기본 케이스 누락 (Missing Default Case in Multiple Condition Expression)](https://cwe.mitre.org/data/definitions/478.html)
* [CWE-484	Switch에서 Break 문 생략 (Omitted Break Statement in Switch)](https://cwe.mitre.org/data/definitions/484.html)
* [CWE-550	민감한 정보를 포함하는 서버 생성 오류 메시지 (Server-generated Error Message Containing Sensitive Information)](https://cwe.mitre.org/data/definitions/550.html)
* [CWE-636	안전하게 실패하지 않음 ('실패 시 열림', Not Failing Securely ('Failing Open'))](https://cwe.mitre.org/data/definitions/636.html)
* [CWE-703	예외 조건의 부적절한 검사 또는 처리 (Improper Check or Handling of Exceptional Conditions)](https://cwe.mitre.org/data/definitions/703.html)
* [CWE-754	비정상적이거나 예외적인 조건에 대한 부적절한 검사 (Improper Check for Unusual or Exceptional Conditions)](https://cwe.mitre.org/data/definitions/754.html)
* [CWE-755	예외 조건의 부적절한 처리 (Improper Handling of Exceptional Conditions)](https://cwe.mitre.org/data/definitions/755.html)
* [CWE-756	사용자 정의 오류 페이지 누락 (Missing Custom Error Page)](https://cwe.mitre.org/data/definitions/756.html)
