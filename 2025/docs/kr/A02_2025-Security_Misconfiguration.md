<link rel="stylesheet" href="../../assets/css/RC-stylesheet.css" />

# A02:2025 보안 설정 오류 (Security Misconfiguration) ![icon](../../assets/TOP_10_Icons_Final_Security_Misconfiguration.png){: style="height:80px;width:80px" align="right"}


## 배경 (Background). 

이전 버전의 #5에서 상승하여, 테스트된 애플리케이션의 100%가 어떤 형태의 설정 오류를 가지고 있는 것으로 발견되었으며, 평균 발생률은 3.00%이고 이 위험 카테고리의 공통 취약점 열거(Common Weakness Enumeration, CWE)가 719k건 이상 발생했습니다. 고도로 구성 가능한 소프트웨어로의 더 많은 전환과 함께, 이 카테고리가 상승하는 것은 놀라운 일이 아닙니다. 주목할 만한 CWE에는 *CWE-16 구성 (Configuration)* 및 *CWE-611 XML 외부 엔티티 참조의 부적절한 제한 (Improper Restriction of XML External Entity Reference, XXE)*이 포함됩니다.


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
   <td>16
   </td>
   <td>27.70%
   </td>
   <td>3.00%
   </td>
   <td>100.00%
   </td>
   <td>52.35%
   </td>
   <td>7.96
   </td>
   <td>3.97
   </td>
   <td>719,084
   </td>
   <td>1,375
   </td>
  </tr>
</table>



## 설명 (Description). 

보안 설정 오류는 시스템, 애플리케이션 또는 클라우드 서비스가 보안 관점에서 잘못 설정되어 취약점을 만드는 경우입니다.

애플리케이션은 다음 경우 취약할 수 있습니다:



* 애플리케이션 스택의 모든 부분에서 적절한 보안 강화가 누락되었거나 클라우드 서비스의 권한이 부적절하게 구성된 경우.
* 불필요한 기능이 활성화되거나 설치된 경우(예: 불필요한 포트, 서비스, 페이지, 계정, 테스트 프레임워크 또는 권한).
* 기본 계정과 해당 암호가 여전히 활성화되어 있고 변경되지 않은 경우.
* 과도한 오류 메시지를 가로채는 중앙 구성이 부족한 경우. 오류 처리가 스택 추적 또는 기타 과도하게 정보가 많은 오류 메시지를 사용자에게 공개합니다.
* 업그레이드된 시스템의 경우, 최신 보안 기능이 비활성화되었거나 안전하게 구성되지 않은 경우.
* 불안전한 구성을 초래하는 하위 호환성의 과도한 우선순위 지정.
* 애플리케이션 서버, 애플리케이션 프레임워크(예: Struts, Spring, ASP.NET), 라이브러리, 데이터베이스 등의 보안 설정이 안전한 값으로 설정되지 않은 경우.
* 서버가 보안 헤더 또는 지시문을 보내지 않거나 안전한 값으로 설정되지 않은 경우.

일관되고 반복 가능한 애플리케이션 보안 구성 강화 프로세스 없이는 시스템이 더 높은 위험에 처해 있습니다.


## 예방 방법 (How to prevent). 

다음을 포함하는 안전한 설치 프로세스를 구현해야 합니다:



* 적절하게 잠긴 다른 환경을 빠르고 쉽게 배포할 수 있도록 하는 반복 가능한 강화 프로세스. 개발, QA 및 프로덕션 환경은 모두 동일하게 구성되어야 하며, 각 환경에서 다른 자격 증명이 사용되어야 합니다. 이 프로세스는 새로운 안전한 환경을 설정하는 데 필요한 노력을 최소화하기 위해 자동화되어야 합니다.
* 불필요한 기능, 구성 요소, 문서 또는 샘플이 없는 최소 플랫폼. 사용하지 않는 기능 및 프레임워크를 제거하거나 설치하지 마세요.
* 패치 관리 프로세스의 일부로 모든 보안 노트, 업데이트 및 패치에 적합한 구성을 검토하고 업데이트하는 작업(참조 [A03:2025-](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)소프트웨어 공급망 실패 (Software Supply Chain Failures)). 클라우드 저장소 권한(예: S3 버킷 권한)을 검토하세요.
* 세분화된 애플리케이션 아키텍처는 세분화, 컨테이너화 또는 클라우드 보안 그룹(ACL)을 통해 구성 요소 또는 테넌트 간의 효과적이고 안전한 분리를 제공합니다.
* 클라이언트에게 보안 지시문 전송, 예: 보안 헤더 (Security Headers).
* 모든 환경에서 구성 및 설정의 효과를 검증하는 자동화된 프로세스.
* 백업으로 과도한 오류 메시지를 가로채는 중앙 구성을 사전에 추가하세요.
* 이러한 검증이 자동화되지 않은 경우, 최소한 연간 수동으로 검증해야 합니다.
 

## 공격 시나리오 예 (Example attack scenarios). 

**시나리오 #1:** 애플리케이션 서버가 프로덕션 서버에서 제거되지 않은 샘플 애플리케이션과 함께 제공됩니다. 이러한 샘플 애플리케이션에는 공격자가 서버를 손상시키는 데 사용하는 알려진 보안 결함이 있습니다. 이러한 애플리케이션 중 하나가 관리 콘솔이고 기본 계정이 변경되지 않았다고 가정하면, 공격자는 기본 암호로 로그인하여 제어권을 얻습니다.

**시나리오 #2:** 서버에서 디렉토리 목록이 비활성화되지 않았습니다. 공격자는 단순히 디렉토리를 나열할 수 있다는 것을 발견합니다. 공격자는 컴파일된 Java 클래스를 찾아 다운로드하고, 이를 역컴파일하고 역공학하여 코드를 봅니다. 그런 다음 공격자는 애플리케이션에서 심각한 접근 제어 결함을 찾습니다.

**시나리오 #3:** 애플리케이션 서버의 구성이 스택 추적과 같은 상세한 오류 메시지를 사용자에게 반환하도록 허용합니다. 이것은 잠재적으로 민감한 정보나 취약한 것으로 알려진 구성 요소 버전과 같은 기본 결함을 노출합니다.

**시나리오 #4:** 클라우드 서비스 제공자(Cloud Service Provider, CSP)는 기본적으로 인터넷에 공유 권한을 열어두는 것으로 설정됩니다. 이것은 클라우드 저장소 내에 저장된 민감한 데이터에 액세스할 수 있게 합니다.


## 참고 자료 (References). 

* OWASP 테스트 가이드: 구성 관리 (Configuration Management)
* OWASP 테스트 가이드: 오류 코드 테스트 (Testing for Error Codes)
* 애플리케이션 보안 검증 표준 5.0.0 (Application Security Verification Standard 5.0.0)
* NIST 일반 서버 강화 가이드 (NIST Guide to General Server Hardening)
* CIS 보안 구성 가이드/벤치마크 (CIS Security Configuration Guides/Benchmarks)
* Amazon S3 버킷 발견 및 열거 (Amazon S3 Bucket Discovery and Enumeration)
* ScienceDirect: 보안 설정 오류 (Security Misconfiguration)


## 매핑된 CWE 목록 (List of Mapped CWEs)

* [CWE-5 J2EE 설정 오류: 암호화 없이 데이터 전송 (J2EE Misconfiguration: Data Transmission Without Encryption)](https://cwe.mitre.org/data/definitions/5.html)

* [CWE-11 ASP.NET 설정 오류: 디버그 바이너리 생성 (ASP.NET Misconfiguration: Creating Debug Binary)](https://cwe.mitre.org/data/definitions/11.html)

* [CWE-13 ASP.NET 설정 오류: 구성 파일의 암호 (ASP.NET Misconfiguration: Password in Configuration File)](https://cwe.mitre.org/data/definitions/13.html)

* [CWE-15 시스템 또는 구성 설정의 외부 제어 (External Control of System or Configuration Setting)](https://cwe.mitre.org/data/definitions/15.html)

* [CWE-16 구성 (Configuration)](https://cwe.mitre.org/data/definitions/16.html)

* [CWE-260 구성 파일의 암호 (Password in Configuration File)](https://cwe.mitre.org/data/definitions/260.html)

* [CWE-315 쿠키에 민감한 정보의 평문 저장 (Cleartext Storage of Sensitive Information in a Cookie)](https://cwe.mitre.org/data/definitions/315.html)

* [CWE-489 활성 디버그 코드 (Active Debug Code)](https://cwe.mitre.org/data/definitions/489.html)

* [CWE-526 환경 변수를 통한 민감한 정보 노출 (Exposure of Sensitive Information Through Environmental Variables)](https://cwe.mitre.org/data/definitions/526.html)

* [CWE-547 하드코딩된 보안 관련 상수 사용 (Use of Hard-coded, Security-relevant Constants)](https://cwe.mitre.org/data/definitions/547.html)

* [CWE-611 XML 외부 엔티티 참조의 부적절한 제한 (Improper Restriction of XML External Entity Reference)](https://cwe.mitre.org/data/definitions/611.html)

* [CWE-614 'Secure' 속성 없이 HTTPS 세션의 민감한 쿠키 (Sensitive Cookie in HTTPS Session Without 'Secure' Attribute)](https://cwe.mitre.org/data/definitions/614.html)

* [CWE-776 DTD에서 재귀적 엔티티 참조의 부적절한 제한 ('XML 엔티티 확장', Improper Restriction of Recursive Entity References in DTDs ('XML Entity Expansion'))](https://cwe.mitre.org/data/definitions/776.html)

* [CWE-942 신뢰할 수 없는 도메인과의 허용적 크로스 도메인 정책 (Permissive Cross-domain Policy with Untrusted Domains)](https://cwe.mitre.org/data/definitions/942.html)

* [CWE-1004 'HttpOnly' 플래그 없이 민감한 쿠키 (Sensitive Cookie Without 'HttpOnly' Flag)](https://cwe.mitre.org/data/definitions/1004.html)

* [CWE-1174 ASP.NET 설정 오류: 부적절한 모델 검증 (ASP.NET Misconfiguration: Improper Model Validation)](https://cwe.mitre.org/data/definitions/1174.html)
